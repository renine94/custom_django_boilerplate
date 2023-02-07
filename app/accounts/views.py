from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return JsonResponse('hello world!', safe=False)


def index2(request):
    context = {
        'name': 'kyle',
    }
    return render(request, 'base.html', context)
