from django.shortcuts import render
import json

#rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import food_details
from django.core import serializers



@api_view(["GET"])
def list_menu_items(request):
    return_data=json.loads(serializers.serialize("json",food_details.objects.all()))
    
    return Response(return_data)

