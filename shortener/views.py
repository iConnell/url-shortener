from django.shortcuts import render
import socket
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Link
from django.shortcuts import redirect
import random

# Create your views here.


@api_view(['POST'])
def createShortUrlView(request):
    longUrl = request.data["url"]
    
    sample = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
    shortUrl = ''.join(random.sample(sample, 6))

    Link.objects.create(longUrl=longUrl, shortUrl=shortUrl)
    
    host = request.get_host()
    shortUrl = 'http://' + host + '/' + shortUrl


    return Response(shortUrl, 200)

@api_view(['GET'])
def redirectView(request, shortUrl):
    try:
        obj = Link.objects.get(shortUrl=shortUrl)
    except Link.DoesNotExist:
        return Response({"msg":"Url does not exist"}, 404)

    if obj is not None:
        return redirect(obj.longUrl)