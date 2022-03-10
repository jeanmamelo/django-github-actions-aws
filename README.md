# Django plus GitHub Actions plus AWS

A simple demonstration on how to set up a CI/CD pipeline with GitHub Actions and AWS Elastic Beanstalk using a Python project built using Django framework.

## Getting started

Assuming you already have [Django](https://www.djangoproject.com/) installed:

```shell
python manage.py runserver
```

## Project structure

```
django-github-actions-aws/
    .envrc
    manage.py
    requirements.txt
    .ebextensions/
        eb.config
    .github/workflows/
        build_test.yml
    core/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        migrations/
            __init__.py
    django_github_actions_aws/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

These files are:

- The outer django-github-actions-aws/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

- .envrc: Used to manage environment variables.

- manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in [django-admin and manage.py](https://docs.djangoproject.com/en/4.0/ref/django-admin/).

- requirements.txt: Is the file that contains the application external dependencies.

- The inner .ebextensions/ directory is where lies the Elastic Beanstalk configurations.

- .ebextensions/eb.config: Is an Elastic Beanstalk configuration file itself.

- The inner .github/workflows/ directory is where lies the GitHub Actions workflows configuration files.

- .github/workflows/build_test.yml: Is a workflow file that GitHub actions will use to execute the steps.

- The inner core/ directory is the actual application folder.

- The inner django_github_actions_aws/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. django_github_actions_aws.urls).

- django_github_actions_aws/__init __.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.

- django_github_actions_aws/settings.py: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/4.0/topics/settings/) will tell you all about how settings work.

- django_github_actions_aws/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/).

- django_github_actions_aws/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/) for more details.
