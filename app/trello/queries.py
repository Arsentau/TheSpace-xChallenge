from . import utilities
from django.conf import settings
from typing import List
import random
from exceptions import appExceptions

labels_map = {
   "Mantainance": settings.TRELLO_LABEL_ID_MANTAINANCE,
   "Research": settings.TRELLO_LABEL_ID_RESEARCH,
   "Test": settings.TRELLO_LABEL_ID_TEST
}

def get_board_members_query():
   query = {
      'key': settings.TRELLO_KEY,
      'token': settings.TRELLO_TOKEN
   }
   return query

def set_todo_query(name:str, desc:str):
   utilities.title_validator(name, 30)
   query = {
      "name": name,
      "desc": desc,
      "pos": "bottom",
      'idList': settings.TRELLO_TODO_ID,
      'key': settings.TRELLO_KEY,
      'token': settings.TRELLO_TOKEN
   }
   return query

def set_bug_query(desc:str, members: List[str]):
   name = utilities.random_title_generator("bug", 7)
   if len(members) == 1:
      member = members[0]
   else:
      member = members[random.randrange(len(members)-1)]

   query = {
      "name": name,
      "desc": desc,
      "pos": "bottom",
      "idLabels": [settings.TRELLO_LABEL_ID_BUG],
      "idMembers": [str(member.get('id'))],
      'idList': settings.TRELLO_BUG_ID,
      'key': settings.TRELLO_KEY,
      'token': settings.TRELLO_TOKEN
   }
   return query

def set_task_query(name:str, label:str, labels_map=labels_map):
   utilities.title_validator(name, 50)
   label_id= labels_map.get(label)
   if not label_id:
      raise appExceptions.BadRequest(detail="Invalid Category")
   query = {
      "name": name,
      "pos": "bottom",
      "idLabels": [label_id],
      'idList': settings.TRELLO_TASK_ID,
      'key': settings.TRELLO_KEY,
      'token': settings.TRELLO_TOKEN
   }
   return query
