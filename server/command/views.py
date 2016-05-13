from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import json

COMMAND_LS_LA = {'command' : 'ls', 'options' : '-la'}

command_json = json.dumps(COMMAND_LS_LA)


# Create your views here.


def index(request):
    return HttpResponse(command_json, content_type='application/json')


def upload_file(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['output_file'])
        return HttpResponse("File uploaded successfully")
    else:
        return HttpResponse("File upload error")


def handle_uploaded_file(f):
    with open('command_output', 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
