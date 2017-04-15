from django import forms
from django.forms import ModelForm
from movies.models import User, Movie, Crew

class LoginForm(forms.Form):
	email = forms.EmailField(label='EMAIL', max_length=30)
	password = forms.CharField(label='PASSWORD', max_length=20)

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','middle_name','last_name','email','password','date_of_birth','sex']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title','description','release_date','language','genre']

class CrewForm(ModelForm):
	class Meta:
		model = Crew
		labels = {'m_id': 'Movies'}
		fields = ['crew_first_name','crew_last_name','role','m_id']

#class RegisterForm(forms.Form):
#	GENDER_CHOICES = (
#		('M', 'Male'),
#		('F', 'Female'),
#		('O', 'Other'),
#	)
#	u_first_name = forms.CharField(label='First Name',max_length=15)
#	u_middle_name = forms.CharField(label='Middle Name',max_length=15,required=False)
#	u_last_name = forms.CharField(label='Last Name',max_length=15)
#	email = forms.EmailField(label='Email',max_length=30)
#	password = forms.CharField(label='Password',max_length=20)
#	dob = forms.DateField(label='Date of Birth')
#	sex = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
