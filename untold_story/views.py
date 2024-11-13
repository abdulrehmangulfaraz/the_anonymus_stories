from django.shortcuts import render
from django.http import FileResponse, Http404
from django.http import JsonResponse
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
        body = request.body.decode('utf-8')
        data = json.loads(body)
        print(data)

        # Check if 'username' exists in data and if the body is not empty
        if 'username' in data and data['username']:
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "failed"})
