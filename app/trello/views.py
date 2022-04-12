from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import trello
from . import serializers
import json

@api_view(['POST'])
def consume_trello(request, action:str):
    data = request.data
    name =  data.get('name')
    label =  data.get('label')
    
    description = data.get('description')
    print(description)
    trelloResponse = trello.post_card_board(action, name, description, label)
    serializer = serializers.TrelloResponse(trelloResponse)
    return Response(serializer.data)