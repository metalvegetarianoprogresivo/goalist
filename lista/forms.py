from django import forms
from follow.models import Profile

# Formulario de registro.
class RegisterForm(forms.Form):
	username = forms.CharField(max_length=20)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput, max_length=20)

class ProfileForm(forms.Form):
	bio = forms.CharField(widget=forms.Textarea)
	avatar = forms.FileField()
	place = forms.CharField(max_length=30)
	website = forms.URLField(initial='http://')