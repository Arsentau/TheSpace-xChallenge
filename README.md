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

> **SECRET_KEY**=xxxxxxxxxxxxxxx
> **DEBUG**=xxxxxxxxxxxxxxx
> **TRELLO_KEY**=xxxxxxxxxxxxxxx
> **TRELLO_TOKEN**=xxxxxxxxxxxxxxx
> **TRELLO_BOARD_ID**=xxxxxxxxxxxxxxx
> **TRELLO_TODO_ID**=xxxxxxxxxxxxxxx
> **TRELLO_BUG_ID**=xxxxxxxxxxxxxxx
> **TRELLO_TASK_ID**=xxxxxxxxxxxxxxx
> **TRELLO_LABEL_ID_MANTAINANCE**=xxxxxxxxxxxxxxx
> **TRELLO_LABEL_ID_RESEARCH**=xxxxxxxxxxxxxxx
> **TRELLO_LABEL_ID_TEST**=xxxxxxxxxxxxxxx
> **TRELLO_LABEL_ID_BUG**=xxxxxxxxxxxxxxx