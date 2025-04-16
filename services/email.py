import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_password_reset_email(user, token):
    context = {
        'full_name': f'{user.first_name} {user.last_name}',
        'token_url': f"{settings.FRONTEND_URL}/forgot-password/{token}/",
        'year': datetime.datetime.now().year
    }
    subject = 'Forgot password request!'
    message = ''
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    html_msg = render_to_string('emails/forget_password.html', context)

    return send_mail(subject, message, from_email, recipient_list, html_message=html_msg)
