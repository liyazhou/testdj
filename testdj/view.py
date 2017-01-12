from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('hello world')


def init(request):
    return HttpResponse('init')


def hello2(request):
    context = {'hello': 'hello world'}
    return render(request, 'hello.html', context)


def helloextends(request):
    context = {'hello': 'hello world'}
    return render(request, 'helloextends.html', context)
