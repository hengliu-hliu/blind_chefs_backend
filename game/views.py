import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random


# Create your views here.

from .models import Deck, Ingredient, Condiment, Action
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

@api_view(['GET'])
def get_ingredient(request, ingredient_id):
    try:
        ingredient = Ingredient.objects.get(id=ingredient_id)
        return Response({
            'id': ingredient.id,
            'name': ingredient.name,
            'type': ingredient.type,
            'value': ingredient.value
        })
    except Ingredient.DoesNotExist:
        return Response(
            {'error': 'Ingredient not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['GET'])
def get_random_item(request):
    # Get counts of all tables
    ingredient_count = Ingredient.objects.count()
    condiment_count = Condiment.objects.count()
    action_count = Action.objects.count()
    total_count = ingredient_count + condiment_count + action_count
    
    # Generate a random number between 1 and total_count
    random_number = random.randint(1, total_count)
    
    # If random number is within ingredient range, get random ingredient
    if random_number <= ingredient_count:
        random_item = random.choice(Ingredient.objects.all())
        return Response({
            'type': 'ingredient',
            'id': random_item.id,
            'name': random_item.name,
            'item_type': random_item.type,
            'value': random_item.value
        })
    # If random number is within condiment range, get random condiment
    elif random_number <= (ingredient_count + condiment_count):
        random_item = random.choice(Condiment.objects.all())
        return Response({
            'type': 'condiment',
            'id': random_item.id,
            'name': random_item.name,
            'value': random_item.value,
            'target': random_item.target
        })
    # Otherwise get random action
    else:
        random_item = random.choice(Action.objects.all())
        return Response({
            'type': 'action',
            'id': random_item.id,
            'name': random_item.name,
            'description': random_item.description,
            'category': random_item.category
        })

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