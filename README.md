# Stardew Valley Villagers API

Author: Fyke Lleva

This API is created using Fast API it is a python library for creating Application Programming Interface. The goal of this API is to provide data related to Villagers in Stardew Valley Game. You can requests:

1. Bachelors Data
2. Bachelorettes Data
3. None Marriage Candidate Data
4. Non-giftable NPCs Data

## Getting Started

### Setting up the environment

1. You need to install fast api using pip

```python
pip install fastapi
```

2. Also need to install server to run the api

```python
pip install uvicorn
```

## Getting Started

### Getting all the villagers

Use this HTTP request to all villagers characters:

```
http://127.0.0.1:8000/
```

### Getting all the villagers using types:

1. Bachelors Data
2. Bachelorettes Data
3. None Marriage Candidate Data
4. Non-giftable NPCs Data

Use this HTTP request to villagers and pass a parameters as {type}:

```
http://127.0.0.1:8000/villagers/{type}
```

### Getting specific villagers:

Use this HTTP request to villagers and pass a parameters as {type} and {id}:

```
http://127.0.0.1:8000/villagers/{type}/{id}
```