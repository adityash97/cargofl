from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core import serializers
# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

class EmployeeDetails(TemplateView):
    def get(self,request):
        employees = Employee.objects.all()
        context ={
            'employees':employees
        }
        return render(request,'employee/employee_details.html',context)



class AddEmployee(TemplateView):
    def get(self,request):
        form = EmployeeForm()
        context = {
            'form':form
        }
        return render(request,'employee/add_employee.html',context)
    def post(self,request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('details_employee'))
        context = {
            'form':form
        }
        return render(request,'employee/add_employee.html',context)

class ViewEmployee(TemplateView):
    def get(self,request,pk):
        empData = Employee.objects.get(pk=pk)
        initial = {
            'employee_first_name':empData.employee_first_name,
            'employee_middle_name':empData.employee_middle_name,
            'employee_last_name':empData.employee_last_name,
            'gender':empData.gender,
            'mobile_number':empData.mobile_number,
            'alternate_mobile_number':empData.alternate_mobile_number,
            'date_of_birth':empData.date_of_birth,
            'email_id':empData.email_id,
            'maritial_staus':empData.maritial_staus,
            'blood_group':empData.blood_group,


        }
        form = EmployeeForm(initial = initial)
        context = {
            'form':form
        }
        return render(request,'employee/view_employee.html',context)
