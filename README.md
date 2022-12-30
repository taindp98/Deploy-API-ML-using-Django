# Deploy an API for the machine learning model using Django REST framework

1. Create the Django project directory

    ```$django-admin startproject mainapp```

2. Setting up the Django application
    
    ```$cd mainapp```

    ```$django-admin startapp monitor```

3. Adding the new application into the settings.py which is just created above

    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',   #new line
        'monitor',          #new line
        ]
    ```

4. Create a new file monitor/urls.py in the application directory and add it into the mainapp/urls.py

5. Load model through apps.py

    Load your machine learning models in apps.py so that when the application starts, the trained model is loaded only once. Otherwise, the trained model is loaded each time an endpoint is called, and then the response time will be slower. 

6. Edit the views.py

    The last step is to update views.py. The views will be mainly responsible for two tasks:

    Process incoming POST requests.
    Make a prediction with the incoming data and give the result as a Response.

7. Launch the API

    ```$ python manage.py runserver```
