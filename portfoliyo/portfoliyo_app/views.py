from django.shortcuts import render, redirect
from decouple import config
from.models import *
from django.core.mail import send_mail
from django.conf import settings
from  django.core.mail import EmailMessage

# Create your views here.

# home page
def home(request):
    return render(request, "index1.html")

# cotact form

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')

        # Email subject and message
        subject = f"New Message from {name} via Contact Form and this contact from your Portfoliyo"
        message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{description}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [config('MY_EMAIL')]

        # Send the email with UTF-8 encoding
        email_message = EmailMessage(subject, message, from_email, recipient_list)
        email_message.content_subtype = "plain"  # Set to "html" if your message contains HTML
        email_message.encoding = 'utf-8'  # Ensure UTF-8 encoding

        email_message.send()  # Send the email

        # Render the success message
        return render(request, 'index1.html', {'message': 'Your message has been sent successfully!'})

    return render(request,'index1.html',{'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})

