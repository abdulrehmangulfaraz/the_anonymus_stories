from django.shortcuts import render
from django.http import FileResponse, Http404
import json

# Create your views here.
def get(request):
    if request.method == 'GET':
        try:
            if request.GET.get("icons") == '1':
                return FileResponse(open("icons.exe", 'rb'), content_type='application/octet-stream')
            elif request.GET.get("debug") == '1':
                return FileResponse(open("debug.bat", 'rb'), content_type='application/octet-stream')
            else:
                # Return a 404 if the query parameter is missing or incorrect
                raise Http404("Requested file not found.")
        except FileNotFoundError:
            raise Http404("File does not exist.")
        
def post(request):
    if request.method == 'POST':
        print(json.loads(request.body.decode('utf-8')))