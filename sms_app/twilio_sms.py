
from twilio.rest import Client
from django.conf import settings

def send_sms(to_number, message_body):
    print(f"SID: {settings.TWILIO_ACCOUNT_SID}")
    print(f"Token: {settings.TWILIO_AUTH_TOKEN}")
    print(f"From: {settings.TWILIO_PHONE_NUMBER}")
    print(f"To: {to_number}")

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message_body,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to_number
    )
    return message.sid
