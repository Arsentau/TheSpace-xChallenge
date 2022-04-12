from rest_framework.decorators import api_view
from rest_framework.response import Response
from exceptions import appExceptions
from . import trello
from . import serializers

@api_view(['POST'])
def consume_trello(request, action:str):
    data = request.data
    name =  data.get('name')
    label =  data.get('label')
    description = data.get('description')
    trelloResponse = trello.post_card_board(action, name, description, label)
    print(trelloResponse)
    try:
        serializer = serializers.TrelloResponse(trelloResponse)
    except:
        raise appExceptions.BadRequest(detail="Bad request from Trello, please try again later.")
    return Response(serializer.data)