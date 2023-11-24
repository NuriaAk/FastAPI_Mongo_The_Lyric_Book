# FastAPI and MongoDB "The Lyric Book"

## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication
+ Deployment

## With this app you can:

+ Create a new song;
+ Read all songs;
+ Find a song by it’s name;
+ Update a song;
+ Delete a song.

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python3 -m venv venv
```

2. Install the modules listed in the `requirements.txt` file:

```console
(venv)$ pip3 install -r requirements.txt
```
3. You also need to start your MongoDB instance locally or using cloud Atlas MongoDB.
4. Start the application:

```console
python main.py
```

The starter listens on port 8000 on address [127.0.0.1](http://127.0.0.1:8000). 


## Testing

To run the tests, run the following command:

```console
(venv)$ pytest
```

You can also write your own tests in the `test_main` directory.  
The test follow by the official support [FastAPI testing guide](https://fastapi.tiangolo.com/tutorial/testing/) for  testing application.

