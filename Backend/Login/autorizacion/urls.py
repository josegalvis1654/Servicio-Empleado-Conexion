from django.urls import path
from .views import LoginView
from .views import VistaProtected

#Sesion

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('vista2/', VistaProtected.as_view(), name='vista2')
]
