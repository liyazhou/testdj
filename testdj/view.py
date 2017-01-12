from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello world')


def init(request):
    return HttpResponse('init')
