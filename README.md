# Tech-Challenge


Project Structure: 

```
.
│   docker-compose.yml
│   README.md
│
├───app
│   │   app.py
│   │   encryptme.py
│   │
│   └───__pycache__
│           encryptme.cpython-38.pyc
│
└───nginx
    │   Dockerfile
    │   index.html
    │   nginx.conf
    │
    └───ssl
        └───certs
                nginx-selfsigned.crt
                nginx-selfsigned.key
.
```

[_docker-compose.yaml_](docker-compose.yaml)

```
 services:
  web:
    build:
      context: nginx
    command: /bin/bash -c "envsubst < /tmp/secure-site.conf > /etc/nginx/conf.d/secure-site.conf && nginx -g 'daemon off;'"
    ports:
      - 443:443
    environment: 
      - FLASK_SERVER_ADDR=backend:5000 
    depends_on:
      - backend
  backend:
    image: digitalocean/flask-helloworld 
    environment: 
      - FLASK_SERVER_PORT=5000
    ports:
     - 5000:5000
    volumes:
      - ./app:/app 
```

In the docker compose we have two services web and backend. The web service one brings up our encrypt and decrypt web page. The backend service brings up the flask image that says Hello from flask. 

## Deploying Application with Docker-Compose: 

```
Command to start the docker containers: docker-compose up -d --build
 => => transferring dockerfile: 32B                                                                                0.0s
 => [internal] load .dockerignore                                                                                  0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/nginx:latest                                                    0.0s
...

 - Network side-content_default      Created                                                                       0.5s
 - Container side-content-backend-1  Started                                                                       2.0s
 - Container side-content-web-1      Started                                                                       2.5s

```

## Expected Results: 

```
Command: Docker ps
CONTAINER ID   IMAGE NAME                      COMMAND                  CREATED         STATUS         PORTS
62687c60ce32   side-content_web                "/docker-entrypoint.…"   7 minutes ago   Up 6 minutes   80/tcp, 0.0.0.0:443->443/tcp   side-content-web-1
ace119fc3c86   digitalocean/flask-helloworld   "python app.py"          7 minutes ago   Up 7 minutes   0.0.0.0:5000->5000/tcp         side-content-backend-1
```
After the application starts, Enter https://localhost:443 in your web browser to bring up the side-content_web container. Then enter localhost:5000 in another web browser to bring up the digitalocean/flask-helloworld container. 

Stop and Remove the containers: 
```
Command: Docker-compose down 
 - Container side-content-web-1      Removed                                                                                                           0.7s
 - Container side-content-backend-1  Removed                                                                                                           0.7s
 - Network side-content_default      Removed                                                                                                           0.6s
```

