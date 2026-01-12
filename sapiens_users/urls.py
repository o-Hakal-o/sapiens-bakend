from django.urls import path
from .views import StudentRegisterView, LoginView

urlpatterns = [
    path('register/student/', StudentRegisterView.as_view(), name='student-register'),
    path('login/', LoginView.as_view(), name='login'), # Esta es la URL del login
]
