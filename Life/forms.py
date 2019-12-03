from django import forms
from .models import Doctor,Department,Patient,Appointment
import datetime as dt
class PostForm_Doctor(forms.ModelForm):
        class Meta:
                model=Doctor
                dept= forms.ModelChoiceField(queryset= Department.objects.all(),  to_field_name="name", widget=forms.Select(attrs={'class':'form-control'}))
                fields=['name','dept','designation','picture','timing','password',]
                labels={
                    'dept':'Department'
                }
                widgets = {
                    'name': forms.TextInput(attrs={'placeholder': '*Enter Fullname','class': "form-control"}),
                    'timing': forms.TextInput(attrs={'placeholder': '*Enter Morning/Afternoon/Evening/Emergency','class': "form-control"}),
                    'designation': forms.TextInput(attrs={'placeholder': '*Enter your designation as specified by the hospital','class': "form-control"}),
                    'password': forms.PasswordInput(attrs={'placeholder': 'Use a strong password', 'size':40,'class': "form-control"}),
                    
                }

class PostForm_Patient(forms.ModelForm):
        class Meta:
                model=Patient
                fields=['name','age','past_record','password','picture']
                widgets = {
                    'name': forms.TextInput(attrs={'placeholder': '*Enter Fullname','class': "form-control"}),
                    'password': forms.PasswordInput(attrs={'placeholder': 'Use a strong password', 'size':40,'class': "form-control"}),
                    'age': forms.NumberInput(attrs={'class':'form-control'}),
                    'past_record': forms.Textarea(attrs={'class':'form-control'})
                }

class Appointment_form(forms.Form):
        HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0,24)]
        dtime=forms.ChoiceField(choices=HOUR_CHOICES,label='Time')
        ddate=forms.DateField(label='Date',widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        dname=forms.ModelChoiceField(label='Doctor Name',queryset= Doctor.objects.all(),  to_field_name="name",widget=forms.Select(attrs={'class':'form-control'}))
     

              