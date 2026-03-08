# mini-rag 

Question answering RAG application using software engineering standards.


### Requirements:
- python 3.10 or later

### Create a python virtual env:
```bash
$ python3 -m venv ~/.venvs/mini-rag-env
```

### Activate the virtual env:
```bash
$ source ~/.venvs/mini-rag-env/bin/activate
```

### Install dependencies

```bash
$ pip install .
```
Note: install ipykernal if you are using vscode

## Setup your environment variables

```bash
$ cp .env.example .env
```
## Run fastapi server
```bash
$ uvicorn main:app --reload --port 5000 
```
## Postman Collection

You can find the postman collection at [assets/min-ragQA-app.postman_collection.json](assets/min-ragQA-app.postman_collection.json)


## Docker compose:

- To install mongodb docker compose image:

```bash
$ cd docker/
$ cp .env.example .env
```

- Update `.env` with your credintials

then run 
```bash
$ docker compose -f docker-compose.yaml up -d

$ sudo docker compose up
```

To stop and remove the running docker images (local if needed):

## 
```bash
$ sudo docker stop $(sudo docker ps -aq)

$ sudo docker rm $(sudo docker ps -aq)
```

If you want to remove the downloaded images and volumes itself
## 
```bash
$ sudo docker rmi $(sudo docker images -q)

$ sudo docker volume rm $(sudo docker volume ls -q)

$ sudo docker system prune --all

```
to rebuild the image 
```bash
$ sudo docker compose up
$ sudo docker compose up -d


```


- To visualize **mongodb** connection use **Studio 3T**, you can download the free community version from [here](https://robomongo.org/download.php) 

- mongodb is connected via **27007** port.

## 
```bash
$ 
```

