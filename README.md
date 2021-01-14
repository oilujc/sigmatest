# Vintage

## Folder structure

    .
    ├── backend 
    │   ├── app          # Local app
    │   |   └── ...
    │   ├── vintage      # Core project folder
    │   |   └── ...
    │   ├── static   
    │   |   └── ...
    │   ├── templates   
    │   |   └── ...
    │   ├── manage.py  
    │   └── Dockerfile   
    ├── frontend
    │   ├── node_modules
    │   |   └── ...
    │   ├── public
    │   |   └── ...
    │   ├── src
    │   |   ├── assets
    |   │   |   └── ...
    │   |   ├── components
    |   │   |   └── ...
    |   │   ├── App.vue
    │   |   └── ...
    │   ├── Dockerfile 
    │   └── ...             
    ├── .env                
    ├── docker-compose.yml
    ├── .gitignore
    └── README.md

## Environment

To start the application it is necessary to include the .env file

## Build

```shell
docker-compose build
```

## Running the application

The application is built with Node.js and already has all environment configured with docker. To start the application you will need `docker` and `docker-compose` installed on the machine. Having that you may run:

```shell
docker-compose up
```

And then the application and database will be started:

```shell
Starting vintage_web_front ... done
Starting vintage_mailhog_1 ... done
Starting vintage_db        ... done
Starting vintage_web_api     ... done
```

The application will be avaible on _PORT 8000_ and 8080_ by default, but it's configurable via `docker-compose.yml` file as an environment variable.

## Running makemigrations

```shell
docker exec -ti vintage_web python /code/manage.py makemigrations
```

## Running empty makemigrations

```shell
docker exec -ti vintage_web python /code/manage.py makemigrations app_name --empty
```

## Running the migrations

```shell
docker exec -ti vintage_web python /code/manage.py migrate
```

## Create super user

```shell
docker exec -ti vintage_web python /code/manage.py createsuperuser

```

