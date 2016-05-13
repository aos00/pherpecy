from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import json


COMMAND_LS_LA = {'command':'ls', 'options':'-la'}
command_json = json.dumps(COMMAND_LS_LA)


def index(request):
    return HttpResponse(command_json, content_type='application/json')

'''
Upload do arquivo obtido de
https://docs.djangoproject.com/en/1.9/topics/http/file-uploads/
'''
def upload_file(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['command_output'])
        return HttpResponse("File uploaded successfully")
    else:
        return HttpResponse("File upload error")


def handle_uploaded_file(f):
    with open('command_output', 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
