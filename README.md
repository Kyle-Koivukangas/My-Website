# This is my personal website

I'm using Vue JS for the front-end and Django for the backend. The two are tied nicely together with django webpack loader, which will tell Django to serve webpack bundles rather than Django templates. 

## Project Clone instructions

Commands to clone project, set up environment and get it running:
```bash
#Git clone project
git clone https://github.com/Kyle-Koivukangas/My-Website-V2.0.git

#Set up Python virtual environment (in main project folder)
cd My-website-V2.0
python -m venv .env

#Activate virtual environment
.\.env\Scripts\activate # ('source env/bin/activate' on mac, 'deactivate' will deactivate the virtual env.)

#Install Django to the virtual environment
pip install django django-webpack-loader

#Install webpack dependencies
cd app/vueapp
npm install

#Run dev build of vue front-end app (make sure you're in the 'vueapp' folder)
npm run dev

#django migrations commands


#Run django back-end in another window (you can run both simoultaneously during development)
cd My-website-V2.0 #(just make sure you're in main django project folder)

#(do your model migrations if needed)
python manage.py makemigrations
python manage.py migrate

python manage.py runserver

```



## Project creation instructions 
(for my own records)

Create django project, set up virtual environment and install pip and npm requirements
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

#TO BE CONTINUED.. Still working out how to get this working correctly...

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

