from django.http import HttpResponse

from testmodel.models import Test


def testdb(request):
    test1 = Test(name='test1 name')
    test1.save()
    return HttpResponse('insert data success')


def get_db(request):
    response1 = ""
    list_result = Test.objects.all()

    response2 = Test.objects.filter(id=1)
    print_set(response2)

    response3 = Test.objects.get(id=1)
    print(response3.name, response3.id)

    response4 = Test.objects.order_by('name')[0:2]
    print_set(response4)

    response5 = Test.objects.order_by('id')
    print_set(response5)

    response6 = Test.objects.filter(name='test1 name').order_by('id')
    print_set(response6)

    for var in list_result:
        response1 += var.name + " "

    response = response1

    return HttpResponse(response)


def print_set(response):
    print(response.values())


def update_db(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'liyazhou'
    test1.save()
    print_set(Test.objects.all())
    Test.objects.filter(id=1).update(name='yazhouli')
    print_set(Test.objects.all())
    Test.objects.all().update(name='lyz')
    print_set(Test.objects.all())
    return HttpResponse('success')


def delete_db(request):
    for i in range(3):
        test1 = Test(name='liyazhou' + str(i))
        test1.save()
    print_set(Test.objects.all())
    test1 = Test.objects.get(id=4)
    test1.delete()
    print_set(Test.objects.all())
    Test.objects.filter(id=5).delete()
    print_set(Test.objects.all())
    Test.objects.all().delete()
    print_set(Test.objects.all())
    return HttpResponse('delete success')
