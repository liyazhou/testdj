from django.http import HttpResponse

from testmodel.models import Test


def testdb(request):
    test1 = Test(name='test1 name')
    test1.save()
    return HttpResponse('insert data success')
