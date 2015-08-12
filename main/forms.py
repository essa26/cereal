from django import forms 
from django.core.validators import RegexValidator
from main.models import Cereal

letter_validator = RegexValidator(r'^[a-zA-Z]*$', 'Please Type Letters')
number_validator = RegexValidator(r'^[0-9]*$', 'Please Type Numbers')

class CerealSearch(forms.Form):
	
	name = forms.CharField(required=True, validators=[letter_validator])#this is a field

class CreateCereal(forms.ModelForm): #creates form from model created 
	class Meta:
		model = Cereal
		fields = '__all__'
		#fields = ['name', 'manufacturer']


class UserSignUp(forms.Form):
	name = forms.CharField(required=True, validators=[letter_validator])
	password = forms.CharField(widget=forms.PasswordInput(), required=True)
	email = forms.CharField(required=True)

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True , widget=forms.PasswordInput())

