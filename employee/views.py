# This conatins all the bussiness logic of this app
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core import serializers
# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Employee,User

from .forms import EmployeeForm


class EmployeeDetails(TemplateView):  # View to Show All the Employee
    def get(self,request):
        employees = Employee.objects.all()
        context ={
            'employees':employees
        }
        return render(request,'employee/employee_details.html',context)



class AddEmployee(TemplateView):  # It contains all the logic to Add an Employee
    def get(self,request):
        form = EmployeeForm()
        context = {
            'form':form
        }
        return render(request,'employee/add_employee.html',context)
    def post(self,request):
        request.POST._mutable = True
        user = User.objects.first()
        request.POST['user'] = user.id
        request.POST._mutable = False

        form = EmployeeForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('details_employee'))
        context = {
            'form':form
        }
        context['form_errors'] = form.errors
        return render(request,'employee/add_employee.html',context)

class ViewEmployee(TemplateView): # This View is to show details of  a perticular Employee
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
