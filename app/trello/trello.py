from typing import List
import requests
import json
from . import queries
from django.conf import settings
from django.core.exceptions import ValidationError

base_url = 'https://api.trello.com/1/'
headers = {"Accept": "application/json"}

def get_board_member():
   url = base_url + "boards/" + settings.TRELLO_BOARD_ID + "/members"
   query = queries.get_board_members_query()
   response = requests.request(
      "GET",
      url,
      params=query
   )
   return response.json()

def post_card_board(action:str, name:str = None, desc: str = None, label:str = None):
   if action != "todo" and action != "bug" and action != "task":
      raise ValidationError(message="Actions can only be todo, bug or task")
   url = base_url + "cards/"
   if action == "todo":
      query = queries.set_todo_query(name, desc)
   if action == "bug":
      members = get_board_member()
      query = queries.set_bug_query(desc, members)
   if action == "task":
      query = queries.set_task_query(name, label)
   response = requests.request(
      "POST",
      url,
      headers=headers,
      params=query
   )
   return response.json()