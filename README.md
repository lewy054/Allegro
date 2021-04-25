# GitHub API

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to use](#how-to-use)
* [Output example](#output-example)

## General info
Choosen task - task 3 Software Engineer

The software was created in python with flask. It can be used as REST API that returns the output in JSON format or with a frontend (it's not too pretty, but that wasn't the main goal).

What can be added?

A lot of things. First of all, more endpoints. GitHub API returns a lot of data that can be used, for example, to create a graph showing how the project was created - all commits connected in order how they were uploaded.

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
        "stars": 0
    },
    "Daily-Journal": {
        "stars": 0
    },
    "FastType": {
        "stars": 0
    },
    "Sort-Visualization": {
        "stars": 0
    },
    "TypeRacer": {
        "stars": 0
    }
}
```

http://127.0.0.1:5000/stars/allegro
```json
6367
```