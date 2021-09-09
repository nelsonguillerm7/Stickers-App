echo "Init commands"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
gunicorn --workers=2 --bind=0.0.0.0:8000 config.wsgi:application
exec "$@"
