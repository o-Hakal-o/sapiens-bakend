from django.urls import path, include
from .views import StudentRegisterView, LoginView, UserProfileView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
urlpatterns = [
    path('register/student/', StudentRegisterView.as_view(), name='student-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    #Rutas de documentación.
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]