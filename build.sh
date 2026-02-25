set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# if [ "$CREATE_SUPERUSER" = "True" ]; then
#     python manage.py createsuperuser --no-input || true
# fi

# python manage.py shell << END
# from django.contrib.auth import get_user_model
# import os

# User = get_user_model()

# if os.getenv("CREATE_SUPERUSER") == "True":
#     username = os.getenv("DJANGO_SUPERUSER_USERNAME")
#     email = os.getenv("DJANGO_SUPERUSER_EMAIL")
#     password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

#     if not User.objects.filter(username=username).exists():
#         User.objects.create_superuser(username, email, password)
# END