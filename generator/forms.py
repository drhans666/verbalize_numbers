from django import forms


class NumberForm(forms.Form):
<<<<<<< Updated upstream
    number = forms.IntegerField(label='Number', required=True)
=======
    number = forms.IntegerField(label='Wpisz liczbę całkowitą', required=True)
>>>>>>> Stashed changes
