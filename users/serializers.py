from rest_framework import serializers

#create your serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=35)
    