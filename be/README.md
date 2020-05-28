# Readme
This document contains a setup guide as well as a basic explanation of functions, settings and general state of the application.

## Module info
- Programmed under Python 3.7.6
- Django & Django rest framework
- Sendgrid
- Env file

## setup guide
1. download a valid version of [Python](https://www.python.org). The application has been tested under [Python 3.7.6](https://www.python.org/downloads/release/python-376/) - backwards and forwards compatibility has not been tested.

2. install [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html). A setup guide can be found in the [Docs](https://virtualenv.pypa.io/en/latest/installation.html)

3. open the project folder in your terminal

4. create a virtual development environment in the project directory (note system specific differences):

**Windows**
```
python -m venv venv
```
**Ubuntu / Mac**
```
python3 -m venv venv
```

5. start the Virtual Development Environment (note system specific differences)

**Windows**
```
venv\Scripts\activate.bat
```
**Ubuntu / Mac**
```
source venv/bin/activate
```

6. update pip
```
pip install --update pip
``` 

7. install packages
```
pip install -r requirements.txt
```
8. create the .env file:
```
cp .env.example .env
```

9. migrate the database schema
```
python manage.py makemigrations
python manage.py migrate
```
10. create a superuser
```
python manage.py createsuperuser
``` 
11. start the server
```
python manage.py runserver
```

If everything works up to here, you have successfully set up the server.

## Additional Setup
### Sendgrid
This application uses in the current version the API of [Sendgrid](https://sendgrid.com). For full functionality of the application in the current version you need a valid account at Sendgrid. The service of Sendgrid is free with 100 emails per day. More emails cost money.

### .env
In the root directory of this application a .env file should be created by point 8 if the setup was successful. Some properties should be adjusted there.
*If you want to make a change to the file, you must restart the server. The changes will not be applied in the running process.*

#### Secret Key - SECRET_KEY
There is a secret key entered. I strongly recommend that you regenerate it.

#### Cookie - Expire [SESSION_COOKIE_VALIDATION_TIME]
Specifies the validity period of the session cookie in minutes. You can change this number as you like.

#### Email-Access Pathes
There are accesses via account activation, password reset and external access. For the functionality of the Django application the paths are irrelevant. They are simply sent along as an email, but do not take on any other internal function.

#### External access - Expires
The variables 'ACTIVATION_KEY_PERIODS_OF_VALIDITY, PW_FORGOTTEN_KEY_PERIODS_OF_VALIDITY, ACCES_KEY_PERIODS_OF_VALIDITY' are used to enter the validity period of an external access. The default string length is 6 characters. I therefore do not recommend a too long validity for the external accesses.

#### Send mails [SEND_MAIL]
For the development I recommend to set this variable to False after the first test phase. In order not to exhaust the 100 free emails or to save your own mailbox, sending the mail itself is optional. At this point I recommend to test it once and then set it to False.

#### Recipient mail [TEST_RECEIVER_MAIL]
If 'Debug = True' and 'SEND_MAIL = True', then mails are sent. The 'TEST_RECEIVER_MAIL' is the default recipient of the email for the test phase. So you can choose arbitrary emails, but you will always get the mail safely to your own mailbox to avoid writing to strangers

#### SENDGRID_API_KEY
After you have registered with Sendgrid, you will receive an API key. You can enter it here. Without the key no mails can be sent

#### SENDER_MAIL
Specifies the default sender email address that a recipient of the email will see.


Translated with www.DeepL.com/Translator (free version)