# sms_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SMSForm
from .twilio_sms import send_sms

# Home page view
def home_view(request):
    return render(request, 'sms_app/home.html')


def send_sms_view(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            to_number = form.cleaned_data['to_number']
            message_body = form.cleaned_data['message_body']
            try:
                message_sid = send_sms(to_number, message_body)
                return HttpResponse(f'SMS sent successfully! Message SID: {message_sid}')
            except Exception as e:
                return HttpResponse(f'Failed to send SMS: {str(e)}')
    else:
        form = SMSForm()

    return render(request, 'sms_app/send_sms.html', {'form': form})
