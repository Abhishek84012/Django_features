# Django_features

## Setup Project using Docker

Just make sure you have installed `docker` in your machine.

### Create a `.env` file

You can just copy the file `.env.template` as `.env` . And please ensure to add your credentials etc.

### Fresh Setup of the Project

Then run the following command to setup project using docker:

```sh 

    docker-compose up -d --build

```

Run the following command to clear all docker exists on your machine(Totally fresh startup):

```sh
    docker system prune -a --volumes
    docker-compose up -d --build

```

### Run Project

http://127.0.0.1:8000/

### Open database on pgadmin4.

Reference <!-- https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5 -->

http://127.0.0.1:5050/login?next=%2F
Username and password take from .env.template file.
 
Then run the following command to get hostname using docker:

```sh
docker ps --all
Get posgres database docker id.
docker inspect docker_id | grep IPAddress
```

step -> create_server - >  fill up information(hostname(get through above command), username, password this take on .env.template) - > save 
