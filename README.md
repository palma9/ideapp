# ideapp
#### Ideapp is an app to save and share ideas built in Django with GraphQl and PostgreSQL.


# Setup
## Prerequirements
- Python3 and Pip
- Docker and Docker Compose.

## Installation

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/palma9/ideapp.git
$ cd ideapp
```

Then turn on the project using docker-compose:
```sh
$ docker-compose build
$ docker-compose up -d
```

And you can test it vía http://127.0.0.1:8000/ or using the [Postman collections](docs/Ideapp.postman_collection.json) and [Enviroments](docs/Ideapp.postman_environment.json).

### For Development

After cloning the repo, have to:

Up the PostgreSQL database via docker-compose:

```sh
$ docker-compose up -d postgres
```

Change the database settings to localhost (Or add postgres to localhost redirection on your /etc/hosts):

```py
DATABASES = {
    'default': {
        ...
        'HOST': 'localhost',
        ...
    }   
}
```
[Optional] Create a virtualenv.

Install pip requirements:

```sh
$ cd app
$ pip install -r requirements.txt
```

And finally, inside app folder, start your server running:

```sh
$ python manage.py runserver 0.0.0.0:8000
```

# Usage

### You can use the generated [Postman collections](docs/Ideapp.postman_collection.json) and [Enviroments](docs/Ideapp.postman_environment.json).
  
First, you need to register or login to get the token.

Then every query or mutation can executed.

Postman doesn't support graphql Subscriptions. So you can use the integrated method in http://localhost:8000

### Or you can use the integrated tool from graphiql in http://localhost:8000/

Subscriptions are not supported by django-graphene and graphiql by default. So A third party library is used to solve this, which removes headers from graphiql interface.

To test methods with a logged user, you can create a super-user vía:

- Via Docker Compose:

```sh
$ docker-compose run app python manage.py createsuperuser
```

- Via development, inside app/ folder:
  
```sh
$ python manage.py createsuperuser
```

and log in it via http://localhost:8000/admin

Then, those credentials will be use on every method.

For Subscription, you need to pass the user_token as a variable.

# Testing

You can find all tests inside app/app_module/tests.py

To test them you only need to run inside app folder:

```sh 
$ py.test
```

# Project Structure
```
    .
    ├── app                         # Django app
    │   ├── base
    │   │   ├── schema.py           # Main graphene schema
    │   │   ├── settings.py         # Django settings variables
    │   │   ├── urls.py             # Urls used by the project
    │   │   └── ...
    │   ├── ideas                   # Module to manage users ideas
    │   │   ├── inputs.py           # Form imput used on mutations
    │   │   ├── models.py           # Idea models
    │   │   ├── mutations.py        # Mutation (Creation, update, deletion methods)
    │   │   ├── schema.py           # Main idea schema. Querys, mutations and subscriptions can be found here
    │   │   ├── tests.py            # Tests files
    │   │   ├── types.py            # Idea types for schema responses
    │   │   └── ...
    │   ├── users                   # User things. Similar to idea's
    │   │   └── ...
    |   └── ...
    ├── docs                        # Projects docs, like postman collections and requirements
    └── ...
```
