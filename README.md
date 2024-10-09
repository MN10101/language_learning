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
- psql -U postgres
- CREATE DATABASE language_learning_db;
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- mkdir D:\language_learning\static
- python manage.py populate_questions
- python manage.py game_questions
- python manage.py runserver
- New Command:
- pip install openai


## Commands MacOS
- python -m venv venv
- source venv/bin/activate
- pip install psycopg2
- pip install postgres
- psql -U postgres
- CREATE DATABASE language_learning_db;
- python manage.py makemigrations
- python manage.py migrate
- mkdir -p /Users/jonathanerasmusdavies/Desktop/edu_02/language_learning_01/static
- In the settings file: STATICFILES_DIRS = [
    "/Users/jonathanerasmusdavies/Desktop/edu_02/language_learning_01/static",]
-  python manage.py populate_questions
-  python manage.py game_questions
-  python manage.py runserver
-  New Command:
- pip install openai
