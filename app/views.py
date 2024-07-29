from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.views import LoginView, LogoutView


class LoginView(LoginView):
    template_name = 'templates/login.html'
    redirect_authenticated_user = True
    # redirect_field_name = ''

class LogoutView(LogoutView):
    # template_name = 'templates/logout.html'
    # redirect_field_name = 'login'
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

