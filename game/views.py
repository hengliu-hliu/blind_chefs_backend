import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

from .models import Deck
from django.views.decorators.http import require_GET

@require_GET
def get_cards(request):
    cards = Deck.objects.all().values('id', 'name', 'image', 'score', 'type')
    return JsonResponse(list(cards), safe=False)

@require_GET
def get_card_by_id(request, id):
    try:
        card = Deck.objects.values('id', 'name', 'image', 'score', 'type').get(id=id)
        return JsonResponse(card, safe=False)
    except Deck.DoesNotExist:
        return JsonResponse({'error': f'Card with id {id} not found.'}, status=404)





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