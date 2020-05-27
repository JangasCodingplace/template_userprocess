# Readme (EN) - General Information

This repository contains a Django Rest application with a React frontend.

Basically a functional authentication system including common user interactions is provided. This template is a composition of some of my snippets.
An email service is provided with Sendgrid. However, this is optional and interchangeable. In the long run, this template serves for a fast prototyping where you can focus on your individual problems.


## Setup
The application is strictly separated into frontend (**fe**) and backend (**be**). The backend should be set up first, followed by the frontend. For the respective setups please read and follow the readmes of the individual folders.

## Functionality
### Login
- The user has the possibility to log in to the platform with his email and password
- by login the user gets automaticaly an info mail

### Registration
- The user registers by entering first name, last name, email and password. He must also agree to the privacy policy.
- After registration an activation link will be sent
- The account is activated as soon as the user clicks on the link

### Password Forgotten 
- by entering an email to the password forgotten field an email will be sent. This will redirect the user to a new password creation page.
- If an account does not exist, no email will be sent. The user does not receive invalid feedback on the frontend

### Profile Edit
- The user has the possibility to edit his given data (first name, last name, email and password)
- To change the email or password, the currently valid password must be entered
- If the user's email is changed, the user will be automatically notified by email to his old email address

### Authentication (general information)
The default authentication is the SessionAuthentication. An HTTP cookie is placed in the user's browser. The validity of the cookie can be edited. Additionally a token must be sent. This token is also stored as a cookie in the user's browser and is set automatically

### Email Access
In the cases of forgotten password and account activation an email with a link to the page will be sent. The user is automatically authenticated via this link and is forwarded to the respective area.
The link has a certain validity period which can be changed.

## Info
This is a non-commercial project!
It was done in my spare time. Also many areas are not tested. The test units are still being implemented.
Errors and tips can be reported to me.
