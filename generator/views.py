from django.shortcuts import render

from generator.verbalization_script import *
from generator.forms import NumberForm


def int_to_str(number):
    if number == 0:
        return 'zero'
    else:
        three_list = stack_threes(number)
        verbalized = verbalize_number(three_list)
        verbalized = check_minus(number, verbalized)
        return verbalized


def main(request):
    form = NumberForm(request.POST or None)
    context = {'form': form}

    if request.method == 'GET' or not form.is_valid():
        return render(request, 'generator/main.html', context)
    data = form.cleaned_data
    number = data['number']
    verbalized = int_to_str(number)
    context['verbalized'] = verbalized
    return render(request, 'generator/main.html', context)
