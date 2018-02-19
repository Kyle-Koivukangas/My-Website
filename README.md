# This is my personal website

I'm using Vue JS for the front-end and Django for the backend. The two are tied nicely together with django webpack loader, which will tell Django to serve webpack bundles rather than Django templates; and Django Rest Framework which provides the API that the front end uses to get info from the database. 

## Project Clone instructions

Commands to clone project, set up environment and get it running:
```bash
#Git clone project:
git clone https://github.com/Kyle-Koivukangas/My-Website-V2.0.git

#Set up Python virtual environment (in main project folder):
cd My-website-V2.0
python -m venv .env
#If you prefer to use virtualenvwrapper then:
mkvirtualenv myWebsite #Or whatever you want to call the virtual env.


#Activate virtual environment:
.\.env\Scripts\activate # ('source env/bin/activate' on mac, 'deactivate' will deactivate the virtual env.)
#Or 
workon myWebsite #if you prefer to use virtualenvwrapper

#Install Django & requirements to the virtual environment:
pip install -r requirements.txt

#Install webpack dependencies:
cd app/vueapp
npm install

#Build the Vue app:
npm run build

#Create database with mezzanine helper function:
cd ../.. #(just make sure you're in base django project directory)
python manage.py createdb

#Do your model migrations if needed, you shouldn't have to right after running createdb though.:
python manage.py makemigrations
python manage.py migrate

#Collect templates and static files:
python manage.py collecttemplates
python manage.py collectstatic
#NOTE: The order matters here, you should run collecttemplates first, then collectstatic;
# this allows the webpack loader template (index.html) to overwrite Mezzanines default index.html.

#NOTE: You'll also need to provide your own SECRET_KEY in the django settings, 
#I have mine saved in a file called secret_info.py that the settings file imports.

#Start 'er up:
python manage.py runserver



## During Development:

#You can run both Django and Vue simoultaneously during development, 
#Use Vue for hotreloading during front-end development and django just to supply the API.
#From the base django directory, run django back-end:
python manage.py runserver

#From 'vueapp' directory, run dev build of vue front-end app in another shell:
npm run dev

#You'll then be able to have a live verion of the vueapp at localhost:8080
#while django provides the API.

```



## Project creation instructions 
(for my own records)

Create django project, set up virtual environment and install pip and npm requirements and install webpack loader so it serves webpack bundles instead of django templates.
```bash
#Create django project 
django-admin startproject myWebsite

cd myWebsite

#Create django app that will house the Vue JS front-end
python manage.py startapp app

cd app

#Create Vue JS app and install npm requirements
vue-cli init webpack vueapp
cd vueapp
npm install

#Additional npm installs to integrate Vue JS with Django
npm install --save-dev webpack webpack-bundle-tracker babel babel-loader

#Then Specify the following variables in Django settings: (reference latest local settings for examples)
# BASE_DIR (location of base directory for Django project), 
# VUE_DIR (Location of Vueapp base directory, not necessary but I did this for convenience),  
# STATIC_ROOT (where you want collectstatic to put all the webpack bundles that will be served),
# STATICFILES_DIRS (where the webpack bundles can be found (in 'dist' folder by default for Vue JS)), 
# WEBPACK_LOADER (settings for webpackloader)

#then you need to add 'webpack_loader' to installed apps and it should be good to go.
```

### Virtual Environment setup
Setup a new Python 3 virtual environment and install the pip requirements.
```bash

#In the Django project's root directory (myWebsite in this case)
python -m venv .env
.\.env\Scripts\activate # ('source env/bin/activate' on mac)
pip install django django-webpack-loader

```



## Sources 

https://github.com/djstein/vue-django-webpack

https://github.com/vuejs-templates/webpack/tree/master/template

https://github.com/owais/django-webpack-loader/tree/master/examples

