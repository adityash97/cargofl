# All Models has been registed here. So that it'll can be accessed by Admin pannel
# Please visit id: root and pass: 123
# http://localhost:8000/admin

from django.contrib import admin

# Register your models here.
from .models import Employee,User

admin.site.register(User)
admin.site.register(Employee)