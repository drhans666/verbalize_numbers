from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from PyICU import *

from generator.verbalization_script import *
from generator.forms import Number


def int_to_str(number):
    three_list = stack_threes(number)
    verbalized = verbalize_number(three_list)
    verbalized = check_minus(number, verbalized)
    return verbalized


def main(request):
    form = Number(request.POST or None)
    context = {'form': form}

    if request.method == 'GET' or not form.is_valid():
        return render(request, 'generator/main.html', context)

    number = request.POST.get('number')
    verbalized = int_to_str(number)
    context['verbalized'] = verbalized
    return render(request, 'generator/main.html', context)
