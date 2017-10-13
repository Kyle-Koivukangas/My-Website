# This is my personal website

I'm using Vue JS for the front-end and Django for the backend. The two are tied nicely together with django webpack loader, which will tell Django to server webpack bundles rather than templates. 


##Project creation instructions 
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

###Virtual Environment setup
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

