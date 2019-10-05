# Pallbot

## System Requirements

- Python 3.6
- Django 2.2.6
- PostgresSQL 10

## Dependencies

- Python 3.6
- virtualenv

### For dependencies

    pip install -r requirements.txt

## Database Management

To setup database the very first time just in development:

    CREATE USER pallbot_development_user PASSWORD 'pallbot_evelopment_password';
    ALTER ROLE pallbot_development_user WITH SUPERUSER;
    CREATE DATABASE pallbot_development WITH OWNER pallbot_development_user;

### Running migrations

To run migrations use the following command:

    ./manage migrate

## Security

As *Nova Coco* We are worry about the security of any of our products. For more reference please review [Pony check up site](https://www.ponycheckup.com/).

## Deployment Instructions

Heroku is our PaaS provider, see the references.

## Admin Panel

The Admin Panel is mounted at:

    localhost:8000/admin

## Generating Super Admin Users

There is a handy task that creates Super Admin Users, you can invoke it with:

    ./manage.py createsuperuser
