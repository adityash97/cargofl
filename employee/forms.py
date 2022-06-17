# This is a Model Form(used model to create it).


from django.forms import ModelForm
from .models import Employee
from employee.widgets import DatePicker
from django.forms import TextInput
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'employee_first_name': TextInput(attrs={'placeholder': 'Please Enter Employee First Name'}),

            'employee_middle_name': TextInput(attrs={'placeholder': 'Please Enter Employee Middle Name'}),

            'employee_last_name': TextInput(attrs={'placeholder': 'Please Enter Employee Last Name'}),


            'mobile_number': TextInput(attrs={'placeholder': 'Please Enter Employee Mobile Number'}),

            'date_of_birth': TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),

            'alternate_mobile_number': TextInput(attrs={'placeholder': 'Please Enter Employee Alternate Mobile Number'}),

            'email_id': TextInput(attrs={'placeholder': 'Please Enter Employee Email Id'}),

 

        }