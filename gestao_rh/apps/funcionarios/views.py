from django.shortcuts import render
from django.http import HttpResponse


def func_view(request):
    return HttpResponse('ola')
