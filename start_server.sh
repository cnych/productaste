python manage_prod.py collectstatic --noinput

uwsgi --ini django_uwsgi.ini
