from myapp.models import Employee
from django import forms
class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
    gender=forms.ChoiceField(choices=[('',"select gender")]+Employee.GENDER_CHOICES)
