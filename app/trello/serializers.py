from rest_framework import serializers

class TrelloResponse(serializers.Serializer):
    id = serializers.CharField()
    name  = serializers.CharField()
    desc = serializers.CharField()
    labels = serializers.ListField()
    idMembers = serializers.ListField()
    url = serializers.CharField()