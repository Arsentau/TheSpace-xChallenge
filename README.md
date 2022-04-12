# The Space-x Challenge

## Technology
This application was created using Python 3.8.0 as programing language and Django 4.0.3 as framework. Besides that, was used Django Rest Framework 3.13.1

On the other hand, this app consumes 2 endpoints of Trello Web Service.

## Functionality
This endpoint can create 3 kinds of cards on a given Trello board, it was developed to make easier create tasks on Trello to people who this could represent a big difficulty. Feel free to join the board with the link bellow:

[This is the link to the board.](https://trello.com/invite/b/xYCFoTUz/7e798045cf41ebcd7af3301c47cb2b28/nanlabsexam)

- In first place a Todo can be created, it represents a business feature that needs implementation.
- In second place a Bug can be created, it represents a problem that needs fixing, it should be assigned to a random member of the board and have the “Bug” label
- Last but not least a Task, it represents some manual work that needs to be done. It counts with just a title and a category (Maintenance, Research, or Test) each corresponding to a label in trello.

## How to Run it locally
Inside of the first level of app folder, where is manage.py file, create a .env file


        SECRET_KEY=xxxxxxxxxxxxxxx
        DEBUG=xxxxxxxxxxxxxxx
        TRELLO_KEY=xxxxxxxxxxxxxxx
        TRELLO_TOKEN=xxxxxxxxxxxxxxx
        TRELLO_BOARD_ID=xxxxxxxxxxxxxxx
        TRELLO_TODO_ID=xxxxxxxxxxxxxxx
        TRELLO_BUG_ID=xxxxxxxxxxxxxxx
        TRELLO_TASK_ID=xxxxxxxxxxxxxxx
        TRELLO_LABEL_ID_MANTAINANCE=xxxxxxxxxxxxxxx
        TRELLO_LABEL_ID_RESEARCH=xxxxxxxxxxxxxxx
        TRELLO_LABEL_ID_TEST=xxxxxxxxxxxxxxx
        TRELLO_LABEL_ID_BUG=xxxxxxxxxxxxxxx

When this file is set run:
- In linux or mac:

    pip install virtualenvwrapper

- In windows:

    pip install virtualenvwrapper-win

- Create a virtual environment:

    mkvirtualenv name

- List virtual environments: **workon**
- Activate virtual environments: **workon name**
- Deactivate virtual environments: **deactivate**

## Install dependencies:
Inside the app folder is requirements.txt, move to that directory with the console and run

    pip install -r requirements.txt

> You must be at the same level that requirements.txt

## Run locally:
With the virtual environment active and requirements installed finally run

    python mangage.py migrate

    python mangage.py runserver

***

## Endpoint Instructions
Local URL = http://127.0.0.1:8000/trello/:type/

**type** could be bug, task or todo (in lowercase)

- Create TODO:
    - type = todo
    - The title is name in the body (is it's name in trello) supose to be short, so it's being validated the length that should be less than 50 characters and not null
    - body:
        
        {
            "name": "Card Title",
            "description": "Here goes the description"
        }
    
    - This TODO card is added to the TODO list as unassigned


- Create BUG:
    - type = todo
    - the title of the bug is created automatically, begins with bug-{randomLetters}-{randomNumbers}, at the momment is created with a function that has to parameters: prefix and quantity of letters and numbers, for this case is setted in 7 but can be easily modified and reused
    - body:
        
        {
            "description": "Here goes the description"
        }
    - This card gets the bug label by default and is assigned to a random member of the board.

- Create TASK:
    - type = task
    - The only 3 labels (categories availables are "Mantainance", "Research" and "Test")
    - body:
        
        {
            "name": "Here goes the description",
            "label": "Mantainance"
        }
    - This card is created with a label in the Task list