from django.urls import path
from django.contrib.auth.views import LoginView
from django_otp.forms import OTPAuthenticationForm

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(authentication_form=OTPAuthenticationForm)),
]