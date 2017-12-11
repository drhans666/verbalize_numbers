from django import forms


class Number(forms.Form):
    number = forms.IntegerField(label='Wpisz liczbę całkowitą', required=True)