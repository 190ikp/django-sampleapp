from django.shortcuts import render
from django.views.generic import *

# Create your views here.

class LoginView():
    pass

# if not logged in, redirect to login page
class EmployeeIndexView(ListView):
    pass

class EmployeeDetailView(DetailView):
    pass

class EmployeeCreateView(CreateView):
    pass

class EmployeeUpdateView(UpdateView):
    pass

class DepartmentCreateView(CreateView):
    pass

