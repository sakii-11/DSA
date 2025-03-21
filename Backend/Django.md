https://www.geeksforgeeks.org/django-interview-questions/
https://codersdaily.in/courses/django-rest-framework-tutorial/django-rest-framework-interview-questions
https://github.com/Devinterview-io/django-interview-questions
https://github.com/Ujjawal-Anand/django-interview

## Creating new project 
```py django-admin startproject projectname   ``

## Creating new app
```py python manage.py startapp appname  ``

## Starting a developement server 
```py python manage.py runserver  ``

## Creating new vir-env
```py python -m venv env(name)  ``

## To run env (name of vir-env)
```py env\Scripts\Activate ``


python manage.py makemigrations
python manage.py migrate
The makemigration command scans the model in your application and generates a new set of migrations based on the model file modifications. This command generates the SQL statement, and when we run it, we obtain a new migration file. After running this command, no tables will be created in the database.

Running migrate command helps us to make these modifications to our database. The migrate command runs the SQL instructions (produced by makemigrations) and applies the database changes. After running this command, tables will be created.


## Include templates
```py {% extends 'template_name.html' %} ```

jango templates not only allow us to pass variables from view to template, but they also provide some programming capabilities like loops, comments, and extensions.  

## Connect to postgres database
Include this in settings.py , by default it is connected to a sqlite db.

```py
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': ‘<database_name>’,
       'USER': '<database_username>',
       'PASSWORD': '<password>',
       'HOST': '<database_hostname_or_ip>',
       'PORT': '<database_port>',
   }
}
``
and then run the migrations cmds.  






## Throttling 
restricts the rate at which clients can make requests to prevent abuse or overuse of the API.  
UserRateThrottle: Limits requests per user.  
AnonRateThrottle: Limits requests per anonymous (unauthenticated) user.  
ScopedRateThrottle: Limits requests based on custom-defined scopes.  
```py
from rest_framework.throttling import UserRateThrottle

class MyAPIView(APIView):
    throttle_classes = [UserRateThrottle]
``


