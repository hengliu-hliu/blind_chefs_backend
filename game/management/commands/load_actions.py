from django.core.management.base import BaseCommand
from game.models import Action

ACTION_DATA = [
    {"name": "Steal", "description": "Steal an card from another player", "category": "action"},
    {"name": "Steal", "description": "Steal an card from another player", "category": "action"},
    {"name": "Sabotage", "description": "Discard an card from another player", "category": "action"},
    {"name": "Sabotage", "description": "Discard an card from another player", "category": "action"},
    {"name": "Sabotage", "description": "Discard an card from another player", "category": "action"},
    {"name": "Sabotage", "description": "Discard an card from another player", "category": "action"},
    {"name": "Nope", "description": "Deny someone else's action card", "category": "action"},
    {"name": "Rinse", "description": "Refresh the pantry", "category": "action"},
    {"name": "Rinse", "description": "Refresh the pantry", "category": "action"},
    {"name": "Rinse", "description": "Refresh the pantry", "category": "action"},
    {"name": "Swap", "description": "Swap an card with another player", "category": "action"},
    {"name": "Swap", "description": "Swap an card with another player", "category": "action"},
    {"name": "Discard", "description": "Discard an card from your hand", "category": "action"},
    {"name": "Discard", "description": "Discard an card from your hand", "category": "action"},
    {"name": "Discard", "description": "Discard an card from your hand", "category": "action"},
    {"name": "Mystery Draw", "description": "Draw a card from the next 3 face down cards in the deck", "category": "action"},
    {"name": "Sabotage", "description": "Discard an card from another player", "category": "action"},
    {"name": "Sabotage", "description": "Discard an card from another player", "category": "action"},
    {"name": "Discard", "description": "Discard an card from your hand", "category": "action"},
    {"name": "Mystery Draw", "description": "Draw a card from the next 3 face down cards in the deck", "category": "action"},
    {"name": "Double Draw", "description": "Draw 2 cards from the pantry", "category": "action"},
    {"name": "Swap", "description": "Swap an card with another player", "category": "action"},
    {"name": "Mystery Draw", "description": "Draw a card from the next 3 face down cards in the deck", "category": "action"},
    {"name": "Double Draw", "description": "Draw 2 cards from the pantry", "category": "action"},
    {"name": "Swap", "description": "Swap an card with another player", "category": "action"},
    {"name": "Blind Draw", "description": "Draw the next card in the draw pile", "category": "action"},
    {"name": "Blind Draw", "description": "Draw the next card in the draw pile", "category": "action"},
    {"name": "Blind Draw", "description": "Draw the next card in the draw pile", "category": "action"},
    {"name": "Feast time", "description": "Give a card in the pantry to another player", "category": "action"},
    {"name": "Feast time", "description": "Give a card in the pantry to another player", "category": "action"},
    {"name": "Thanksgiving", "description": "Give a card in the pantry to each other player", "category": "action"},
    {"name": "Nope", "description": "Deny someone else's action card", "category": "action"},
    {"name": "Mystery Draw", "description": "Draw a card from the next 3 face down cards in the deck", "category": "action"},
]

class Command(BaseCommand):
    help = 'Loads action card data into the database'

    def handle(self, *args, **options):
        # Clear existing data
        Action.objects.all().delete()
        
        # Load actions
        for action_data in ACTION_DATA:
            Action.objects.create(**action_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded action data')) 