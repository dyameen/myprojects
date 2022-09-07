from django import forms
from django.core import validators

#
# def check_age (value):
#     n = int (value)
#     if n<0 or n>100:
#         raise forms.ValidationError ("Enter valid age.")


class contact_form(forms.Form):
    full_name = forms.CharField (initial = 'Full Name',)
    email = forms.EmailField (help_text = 'write your email',)
    subject = forms.CharField (required = True,)
    message = forms.CharField(widget=forms.Textarea)

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
