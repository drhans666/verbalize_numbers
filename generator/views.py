from django.shortcuts import render
<<<<<<< Updated upstream

from PyICU import *

=======

from generator.verbalization_script import *
>>>>>>> Stashed changes
from generator.forms import NumberForm


def int_to_str(number):
    """
    Transforms integer into verbalized string 
    :param number: integer 
    :return: string
    """
    rb = RuleBasedNumberFormat(URBNFRuleSetTag.SPELLOUT, Locale('pl_PL'))
    verbalized = rb.format(int(number))
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
