"""from django import forms
from childapp.models import register


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='lastname')
    
    phone = forms.CharField(label='phone')
    dob = forms.DateField(label='dob')
    
    class Meta:
        model = register  
        fields = ['first_name','last_name','phone','dob']"""