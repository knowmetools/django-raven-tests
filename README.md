# django-raven-tests

Repository for testing issues with raven-python and Django.


## Installation

*Note: We assume Python 3 and virtualenvwrapper are installed.*

First create a new virtual environment and clone the project.

```shell
$ mkproject --python=python3 django-raven-tests
$ git init
$ git remote add origin git@github.com:knowmetools/django-raven-tests
$ git pull origin master
```

To run the project, make the necessary migrations and start the server.

```shell
$ pip install -r requirements.txt
$ ./project/manage.py migrate
$ ./project/manage.py runserver
```

## Endpoints

**`http://localhost:8000/my-app/foo/`**

Responds to any request with the following:

```json
{
  "hello": "world"
}
```
