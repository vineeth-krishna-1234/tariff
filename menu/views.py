from django.shortcuts import render

#rest
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(["GET"])
def list_menu_items(request):
    return Response("hello")

