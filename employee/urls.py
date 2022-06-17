from django.urls import path
from .views import EmployeeDetails,AddEmployee,ViewEmployee
urlpatterns = [
    path('',EmployeeDetails.as_view(),name='details_employee'),
    path('add'or'add/',AddEmployee.as_view(),name='add_employee'),
    path('<int:pk>',ViewEmployee.as_view(),name='view_employee')
    
]