from django.conf import settings
from rest_framework import status
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_message(message, receiver, subject='No Subject', sender=None):
    if not sender:
        sender = settings.ENV['SENDER_MAIL']
    if settings.DEBUG:
        receiver = settings.ENV['TEST_RECEIVER_MAIL']

    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=message
    )

    try:
        sg = SendGridAPIClient(settings.ENV['SENDGRID_API_KEY'])

        if settings.ENV['SEND_MAIL']=='False':
            return status.HTTP_200_OK

        response = sg.send(message)
        return response.status_code

    except Exception as e:
        print(e)
        return False