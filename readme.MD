
  

# About the project

  

The project uses nginx as load balancer over a simple Flask application.

  

By default NGINX uses Round Robin to load balance traffic, directing it sequentially to next configured server in the upstream group. But since we are using Docker we don't need to explicitly mention it in our `nginx.conf` file.

  

## Folder structure

  

`app` folder for the Flask application with Dockerfile inside it to build it.

Then on the root level `docker-compose.yaml` to handle the multi-container deployment with `nginx.conf` defined there.

  

## start up the container

  

`docker compose up -d --build --scale app=x`

  

  

where `x` is the number of instances of the application.

  

## stop the container

  

`docker compose down`