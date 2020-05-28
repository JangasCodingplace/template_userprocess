from django.conf import settings
from django.template.loader import get_template
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.utils.timezone import now

from django.db.models.signals import (
    post_save,
    pre_save
)
from django.contrib.auth.signals import user_logged_in

from User.TemporaryAccess.models import TemporaryAccess

from .email import send_message

User = get_user_model()

@receiver(post_save, sender=TemporaryAccess)
def send_mail_to_user(*args, **kwargs):
    access = kwargs['instance']
    if kwargs['created']:
        context = {
            'access':access
        }
        if access.group == 'pw':
            subject = 'Password forgotten'
            raw_mail_body = get_template('password_forgotten.html')
        elif access.group == 'l':
            subject = 'Get Access with Email'
            raw_mail_body = get_template('tmp_access.html')
        else:
            subject = 'Your Account Activation'
            raw_mail_body = get_template('registration.html')
        mail = raw_mail_body.render(context)
        
        if settings.DEBUG:
            print(mail)
        send_message(
            message = mail,
            receiver = access.user.email,
            subject = subject
        )


@receiver(pre_save, sender=User)
def send_chainge_mail_to_user(*args,**kwargs):
    user = kwargs['instance'] 
    try:
        prev_user = User.objects.get(pk=user.pk)
    except User.DoesNotExist:
        return
    
    if user.email != prev_user.email:
        """
        Send Emailchange Mail
        """
        email_change_info_mail_body = get_template('email_chainged.html')
        context = {
            'user':user,
            'prev_user':prev_user
        }
        subject = 'Your Email has changed!'
        mail = email_change_info_mail_body.render(context)
        if settings.DEBUG:
            print(mail)
        send_message(
            message = mail,
            receiver = prev_user.email,
            subject = subject
        )

        

@receiver(user_logged_in)
def send_login_info_mail(*args,**kwargs):
    user = kwargs['user']
    if user.last_login is not None:
        """
        Send Logininfo Mail
        """
        login_info_mail_body = get_template('login_info.html')
        context = {
            'user':user,
            'date':now()
        }
        subject = 'Login Info'
        mail = login_info_mail_body.render(context)
        if settings.DEBUG:
            print(mail)
        send_message(
            message = mail,
            receiver = user.email,
            subject = subject
        )
