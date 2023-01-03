SET DJANGO_SUPERUSER_USERNAME=admin
SET DJANGO_SUPERUSER_PASSWORD=admin
SET DJANGO_SUPERUSER_EMAIL='mkisunko@gmail.com' 
python manage.py makemigrations services
python manage.py migrate
python manage.py createsuperuser --no-input
python manage.py runserver