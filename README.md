# ComPod
web app where users can create personalized comedy podcast feeds

# To Install 
#### (_requires python3_)
create and enter virtual environment

`python -m venv env && source env/bin/activate`

install project dependencies

`pip install -r requirements.txt`

# For Local Dev
create a `.env` file in the project root directory (where settings.py is located) and set the following values
```
DEBUG=True
SECRET_KEY=test

EMAIL_HOST_USER=user@gmail.com
EMAIL_HOST_PASSWORD=<gmail_password>
```
[Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)

# To Run
`python manage.py migrate`

`python manage.py runserver`

Navigate to localhost:8000

# Production Environment

