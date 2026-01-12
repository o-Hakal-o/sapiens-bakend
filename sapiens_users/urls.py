from django.urls import path
from .views import StudentRegisterView, LoginView, UserProfileView # <-- Asegúrate de que esté aquí

urlpatterns = [
    path('register/student/', StudentRegisterView.as_view(), name='student-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]