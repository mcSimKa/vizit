call .venv\scripts\activate.bat
SET DJANGO_SUPERUSER_USERNAME=admin
SET DJANGO_SUPERUSER_PASSWORD=admin
SET DJANGO_SUPERUSER_EMAIL='mkisunko@gmail.com' 
python manage.py makemigrations services
python manage.py migrate
python manage.py createsuperuser --no-input
python manage.py loaddata general.yaml 
python manage.py loaddata geodata.yaml 
python manage.py runserver