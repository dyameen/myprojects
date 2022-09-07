from django import forms
from django.core import validators


def check_age (value):
    n = int (value)
    if n<0 or n>100:
        raise forms.ValidationError ("Enter valid age.")


class SignUp (forms.Form):
    first_name = forms.CharField (initial = 'First Name',)
    last_name = forms.CharField ()
    email = forms.EmailField (help_text = 'write your email',)
    Address = forms.CharField (required = False,)
    Technology = forms.CharField (initial = 'Django',disabled = True,)
    age = forms.IntegerField (validators = [check_age])
    fav_no = forms.IntegerField ()
    password = forms.CharField (widget = forms.PasswordInput,validators = [validators.MinLengthValidator (6)])
    re_password = forms.CharField (help_text = 'renter your password',widget = forms.PasswordInput)

    # def clean_password (self):
    #     password = self.cleaned_data['password']
    #     if len (password) < 4:
    #         raise forms.ValidationError ("password is too short")
    #     return password
    #
    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #     print("age from function---",age)
    #     if age > 100 or age<=0:
    #     # if 100 < age <= 0:
    #         raise forms.ValidationError("Enter proper age.")
    #     return age
    #
    # def clean_fav_no(self):
    #
    #     fno = self.cleaned_data['fav_no']
    #     print(fno)
    #     if fno > 100:
    #         raise forms.ValidationError('Enter properly')
    #     return fno
