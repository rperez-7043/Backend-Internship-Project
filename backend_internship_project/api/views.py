import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client


def home(request):
    return redirect('send_sms')

@api_view(['GET', 'POST'])
def send_sms(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        # print("- phone_number:", phone_number)
        # print("- message:", message)

        load_dotenv() 

        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

        client = Client(account_sid, auth_token)

        message_response = client.messages.create(
            to = phone_number,
            from_ = twilio_phone_number,
            body = message)

        return render(request, 'api/sms_form.html', {
                'success': 'SMS sent successfully!',
                'phone_number': '',
                'message': '',
                'message_info': message_response
            })

    return render(
        request=request,
        template_name="api/sms_form.html"
    )