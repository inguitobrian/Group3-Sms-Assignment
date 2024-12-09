# Django SMS Application

# Description
A Django web application for sending SMS messages using Twilio, with a simple web interface for composing and sending text messages.

# Prerequisites
 - Python 3.8+
 - Django
 - Twilio library
 - Twilio account credentials
 
# Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies

 ```rb
pip install django twilio
```
# Configuration

 - Add Twilio credentials to Django settings:

 ```rb
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
```
# Project Structure

 - admin.py: Django admin configuration
 - apps.py: App configuration
 - forms.py: SMS form with validation
 - models.py: Database models (currently empty)
 - twilio_sms.py: Twilio SMS sending logic
 - urls.py: URL routing
 - views.py: Request handling and SMS sending

# Usage

 1. Run the development server:
 ```rb
# bash
python manage.py runserver
```
2. Navigate to the SMS sending page
3. Enter a phone number and message
4. Send SMS
