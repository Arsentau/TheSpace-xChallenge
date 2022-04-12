from typing import List
import requests
from . import queries
from django.conf import settings
from exceptions import appExceptions

base_url = 'https://api.trello.com/1/'
headers = {"Accept": "application/json"}

def get_board_member():
   url = base_url + "boards/" + settings.TRELLO_BOARD_ID + "/members"
   query = queries.get_board_members_query()
   try:
      response = requests.request(
         "GET",
         url,
         params=query
      )
   except:
      raise appExceptions.ServiceUnavailable(detail="Couldn't get board's members, try again later")
   return response.json()

def post_card_board(action:str, name:str = None, desc: str = None, label:str = None):
   if action != "todo" and action != "bug" and action != "task":
      raise appExceptions.BadRequest(detail="Invalid parameter on URI")
   url = base_url + "cards/"
   if action == "todo":
      if not desc:
         raise appExceptions.BadRequest(detail="A description is needed to create this To Do.")
      query = queries.set_todo_query(name, desc)
   if action == "bug":
      if not desc:
         raise appExceptions.BadRequest(detail="A description is needed to create this Bug.")
      members = get_board_member()
      query = queries.set_bug_query(desc, members)
   if action == "task":
      if not label:
         raise appExceptions.BadRequest(detail="A label is needed to create this Task.")
      query = queries.set_task_query(name, label)
   response = requests.request(
      "POST",
      url,
      headers=headers,
      params=query
   )
   return response.json()