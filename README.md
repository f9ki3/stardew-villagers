# Stardew Valley Villagers API

Author: Fyke Lleva

This API is created using Fast API it is a python library for creating Application Programming Interface. The goal of this API is to provide data related to Villagers in Stardew Valley Game. You can requests:

1. bachelors Data
2. bachelorettes Data
3. none_marriage_candidates Data
4. non_giftable_npcs Data

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

## How to run the code

1. Open the repository to a text editor like Visual Studio Code or Pycharm
2. Open the terminal and run this command:

```python
uvicorn main:app --reload
```

## How to request the data?

### Getting all the villagers

Use this HTTP request to all villagers characters:

```
http://127.0.0.1:8000/villagers
```

### Getting all the villagers using types:

1. Bachelors
2. Bachelorettes
3. None Marriage Candidate
4. Non-giftable NPCs

Use this HTTP request to villagers and pass a parameters as {type}:

```
http://127.0.0.1:8000/villagers/{type}
```

### Getting specific villagers:

Use this HTTP request to villagers and pass a parameters as {type} and {id}:

```
http://127.0.0.1:8000/villagers/{type}/{id}
```

## Contact

Feel free to reach out if you have any questions or suggestions:

- **Author:** Fyke Lleva
- **Email:** floterina@gmail.com
- **Facebook:** (https://web.facebook.com/FLOZ.STN)
- **Linkedin:** (https://www.linkedin.com/in/fykkkie/)
- **Website:** (https://f9ki3.onrender.com/)
  
Thank you for exploring my Python Fast API!
