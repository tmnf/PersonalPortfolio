from django.core.mail import send_mail
from TF_Site import settings

EMAIl = 'tiagomnf1999@gmail.com'


def send_message(name, email, subject, message):
    subject_form = subject + ' - ' + name
    message_form = message + '\n\n===========================================\n' \
                             'Email de Contacto: ' + email + \
                   "\n==========================================="

    send_mail(
        subject_form,
        message_form,
        settings.EMAIL_HOST_USER,
        (EMAIl,),
        fail_silently=False,
    )
