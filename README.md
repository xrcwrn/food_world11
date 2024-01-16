python --version
django-admin --version
create a new virtual environment using the venv module:
py -m venv venu
activate the virtual environment:
venu\Scripts\activate.bat

pip install django
pip install djangorestframework

django-admin startproject restapi

To run the Django development server
python manage.py runserver

To migrate
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

