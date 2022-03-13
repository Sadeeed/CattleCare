from django.core.mail import send_mail
from django.conf import settings


class EmailService:

    @staticmethod
    def send_signup_email(user):
        send_mail(
            'Welcome to Cattle Care',
            'Your one stop shop for cattle health monitoring',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False, )
