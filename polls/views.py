import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def my_view(request):
    data = {
        "message": "Hello, world!",
        "status": "success"
    }
    return JsonResponse(data)

@csrf_exempt
def raw_post_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON payload
            name = data.get("name")
            age = data.get("age")
            return JsonResponse({"message": f"Received name: {name}, age: {age}"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)