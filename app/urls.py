from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeIndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('detail/<int:pk>/', EmployeeDetailView.as_view(), name='detail'),
    path('register/', EmployeeCreateView.as_view(), name='register'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='update'),
    path('create/department', DepartmentCreateView.as_view(), name='create_department'),
]