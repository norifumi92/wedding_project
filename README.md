# About this project

This project inheritated the template at: https://github.com/heroku/heroku-django-template

## How to run the project locally

To start the project, run the code below:

```bash
python manage.py runserver {IP Address:8000}
```

The collectstatic should be disabled by the command below otherwise an error will occur:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1 -a nori-amira-wed-project
```

## References
1. Python code style shall follow PEP8 standard: https://www.python.org/dev/peps/pep-0008/

2. To add animation, this project employed Animate.css:
https://github.com/daneden/animate.css