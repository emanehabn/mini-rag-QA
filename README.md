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
## 
```bash
$ 
```

