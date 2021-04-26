from django.shortcuts import render
from .models import *


def test(request):
    return render(request, 'testtest/test.html', {'rubrics': Rubric.objects.all()})


def get_rubric(request):
    pass
