from django.shortcuts import render
from django.http import HttpResponse


def salam(request):
    response = HttpResponse("salam")
    return response

