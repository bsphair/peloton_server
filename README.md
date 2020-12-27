# Peloton Server

This is the backend for the Peloton project.

## Run with Docker

#### Build the images
```bash
docker-compose build
 ```

#### Run the project
```bash
docker-compose up
```

#### Stop the project
```bash
docker-compose down
```

## Run without Docker
```bash
 uvicorn main:app --reload
 ```