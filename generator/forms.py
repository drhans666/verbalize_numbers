from django import forms


class NumberForm(forms.Form):
    number = forms.IntegerField(label='Number', required=True,
                                max_value=999999999999999)