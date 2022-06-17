from django.forms import ModelForm
from .models import Employee
from employee.widgets import DatePicker
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # widgets = {
        #     'date_of_birth': DatePicker
        # }