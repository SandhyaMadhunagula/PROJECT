from django.shortcuts import render
from django.http import HttpResponse
def fun(response):
    return HttpResponse("This is first project")
def home(response):
    return HttpResponse("this is second statement")