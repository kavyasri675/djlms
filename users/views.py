from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def newData(request):
    user = User.objects.get(id=1)
    serializer = UserSerializer(user)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData,content_type='application/json')