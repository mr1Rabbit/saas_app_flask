---
#### 1.  Running the Flask Application
---

## Build and start everything with Docker Compose

```
docker-compose up --build
```

## Visit the site in your browser

http://localhost:8000/

## Restart Docker Compose

```
# Press CTRL+C a few times
docker-compose stop
docker-compose up
```

## View all of your Docker images

**Run this in a second terminal tab.**

```
docker images
```

## View running Docker containers

**Run this in a second terminal tab.**
Both commands below do basically the same thing.

```
docker-compose ps
docker ps
```

## Stop Docker Compose

```
# Press CTRL+C a few times and ensure everything has stopped by running:
docker-compose stop
```

---

#### 2. Dealing with Configuration Settings

---

## Start everything with Docker Compose

```
docker-compose up
```

## Make a configuration change and check it in your browser

To be filled later

## Create instance/settings.py

To be filled later

## Stop Docker Compose

```
# Press CTRL+C a few times and ensure everything has stopped by running:
docker-compose stop
```

## Clean up our Docker mess

### Remove stopped containers

```
docker-compose rm -f
```

### Remove "dangling" images

```
docker rmi -f $(docker images -qf dangling=true)
```
