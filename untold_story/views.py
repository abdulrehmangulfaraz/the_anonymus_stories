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
        try:
            # Decode and load the JSON data
            body = request.body.decode('utf-8').strip()
            if not body:
                return JsonResponse({"status": "failed", "message": "Empty body received"}, status=400)

            data = json.loads(body)

            # Check for the 'data' object with 'username' and 'content'
            if 'data' in data and 'username' in data['data'] and 'content' in data['data']:
                username = data['data']['username']
                content = data['data']['content']

                # Ensure username and content are not empty
                if username and content:
                    return JsonResponse({"status": "success"})
                else:
                    return JsonResponse({"status": "failed", "message": "Username or content is empty"}, status=400)
            else:
                return JsonResponse({"status": "failed", "message": "Missing 'data', 'username', or 'content' fields"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"status": "failed", "message": "Invalid JSON format"}, status=400)

        except Exception as e:
            return JsonResponse({"status": "failed", "message": str(e)}, status=500)
