## Commands Windows

- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- pip install psycopg2
- pip install psycopg
- pip show psycopg2
- pip show psycopg
- $env:Path
- $env:Path += ";C:\Program Files\PostgreSQL\16\bin"
- psql -U postgreslscle
- CREATE DATABASE language_learning_db;
- python manage.py createsuperuser
- mkdir D:\language_learning\static
- python manage.py german_questions_data
- python manage.py populate_questions
- python manage.py game_questions
- python manage.py it_questions
- pip install whitenoise
- python manage.py collectstatic --clear
- rm -rf /usr/local/django_app/staticfiles
- mkdir -p /usr/local/django_app/static
- python manage.py collectstatic
- python manage.py makemigrations
- python manage.py migrate
- pip freeze > requirements.txt
- python manage.py runserver
- Optional:
- pip install openai
- Uninstalling all global Python packages: pip freeze > temp.txt && for /F "delims=" %i in (temp.txt) do pip uninstall -y %i
- python manage.py clear_questions

=======

## Commands MacOS

- python -m venv venv
- source venv/bin/activate
- pip install psycopg2
- pip install postgres
- psql -U postgres
- CREATE DATABASE language_learning_db;
- mkdir -p /Users/jonathanerasmusdavies/Desktop/edu_02/language_learning_01/static
- In the settings file: STATICFILES_DIRS = [
  "/Users/jonathanerasmusdavies/Desktop/edu_02/language_learning_01/static",]
  python manage.py german_questions_data
- python manage.py populate_questions
- python manage.py game_questions
- python manage.py makemigrations
- pip install whitenoise
- python manage.py migrate
- python manage.py runserver
- New Command:
  "/Users/jonathanerasmusdavies/Desktop/edu_02/language_learning_01/static",]
- python manage.py populate_questions
- python manage.py game_questions
- python manage.py collectstatic --clear
- rm -rf /usr/local/django_app/staticfiles
- mkdir -p /usr/local/django_app/static
- python manage.py collectstatic
- pip freeze > requirements.txt
- python manage.py runserver
- Optional:
- pip install openai
- Uninstalling all global Python packages: pip freeze | xargs pip uninstall -y
- python manage.py clear_questions

=======

## Commands For adding the database circumeo

- export LANGUAGE_LEARNING_DB='language_learning_db'
- export POSTGRES_USER='postgres'
- export POSTGRES_PASSWORD='mamo'
- export DB_HOST='9ly-passionate-heisenberg.circumeo-apps.net'
- export DB_PORT='5432'
- echo ~
- touch .bashrc
- echo "export LANGUAGE_LEARNING_DB='language_learning_db'" >> .bashrc
- echo "export POSTGRES_USER='postgres'" >> .bashrc
- echo "export POSTGRES_PASSWORD='mamo'" >> .bashrc
- echo "export DB_HOST='9ly-passionate-heisenberg.circumeo-apps.net'" >> .bashrc
- echo "export DB_PORT='5432'" >> .bashrc
- source .bashrc
- echo $LANGUAGE_LEARNING_DB
- echo $POSTGRES_USER
- echo $POSTGRES_PASSWORD
- echo $DB_HOST
- echo $DB_PORT

=======

## Commands For circumeo

- pip install --user virtualenv
- virtualenv myenv
- source myenv/bin/activate
- pip install django psycopg2
