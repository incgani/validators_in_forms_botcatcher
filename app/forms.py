from django import forms
from django.core import validators

def a(value):
    if value[0]=='a':
        raise forms.ValidationError('enter a valid name')
    
def b(value):
    if len(value)<=5:
        raise forms.ValidationError('enter a valid name')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[a,b])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,required=False,widget=forms.HiddenInput)
    mobile=forms.CharField(validators=[validators.MaxLengthValidator(10),validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('not matched')
        
    # def clean_age(self):
    #     a=self.cleaned_data['age'] # we cant use for validation, if we use mean if it is not valid its returns 'NONE' as value
    #     if a<=10:
    #         raise forms.ValidationError('not matched')

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('botcatcher')















