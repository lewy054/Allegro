# GitHub api

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to use](#how-to-use)
* [Output example](#output-example)

## General info


## Technologies
Project is created with:
* Python 3.9.2
* Flask


## Setup
Download dependencies from requirements.txt
```
pip3 install -r requirements.txt
```
Run main.py

By default, server starts at http://127.0.0.1:5000/

## How to use
If you want to use this as REST API:

You have to make a GET requests to:

http://127.0.0.1:5000/repos/\<username> - repository names and their stars

http://127.0.0.1:5000/stars/\<username> - sum of all user stars

Example:

http://127.0.0.1:5000/repos/allegro


Other way is to use it with frontend, then just go to http://127.0.0.1

## Output Example

http://127.0.0.1:5000/repos/lewy054

```json
{
    "Allegro": {
        "watchers": 0
    },
    "Daily-Journal": {
        "watchers": 0
    },
    "FastType": {
        "watchers": 0
    },
    "Sort-Visualization": {
        "watchers": 0
    },
    "TypeRacer": {
        "watchers": 0
    }
}
```

http://127.0.0.1:5000/stars/allegro
```json
6367
```