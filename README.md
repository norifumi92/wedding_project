# About this project

This project inheritated the template at: https://github.com/heroku/heroku-django-template

## How to run the project locally

To start the project, run the code below:

```bash
python manage.py runserver {IP Address:8000}
```

The collectstatic should be stopped by the command below otherwise an error will occur:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1 -a nori-amira-wed-project
```