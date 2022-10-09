from email.policy import default
from django import forms 


class ExamForm(forms.Form):
    choices= ((1, 'ساده'),(2, 'متوسط'),(3, 'سخت'))

    number = forms.IntegerField(label='تعداد سوالات', initial= 10, min_value=0, max_value= 100,
                             widget=forms.NumberInput(attrs={'class':'form-control'}))
    level= forms.ChoiceField(label='سطح سوالات', choices=choices, initial=2,
                             widget=forms.Select(attrs={'class':'form-control'}))   

    