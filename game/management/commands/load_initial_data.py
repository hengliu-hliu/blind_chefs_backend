from django.core.management.base import BaseCommand
from game.models import Ingredient, Condiment

INITIAL_DATA = {
    "ingredients": [
        { "name": "Wild Mushroom", "type": "vegetable", "value": 4 },
        { "name": "Venison", "type": "meat", "value": 6 },
        { "name": "Duck Egg", "type": "protein", "value": 4 },
        { "name": "Blueberry", "type": "fruit", "value": 3 },
        { "name": "Walnut", "type": "nut", "value": 4 },
        { "name": "Honeycomb", "type": "sweet", "value": 3 },
        { "name": "Truffle", "type": "vegetable", "value": 6 },
        { "name": "Salmon", "type": "meat", "value": 5 },
        { "name": "Wild Garlic", "type": "vegetable", "value": 3 },
        { "name": "Chestnut", "type": "nut", "value": 4 },
        { "name": "Wild Berry", "type": "fruit", "value": 2 },
        { "name": "Quail", "type": "meat", "value": 5 },
        { "name": "Rainbow Carrot", "type": "vegetable", "value": 3 },
        { "name": "Blackberry", "type": "fruit", "value": 3 },
        { "name": "Kale", "type": "vegetable", "value": 2 },
        { "name": "Hazelnut", "type": "nut", "value": 3 },
        { "name": "Duck Breast", "type": "meat", "value": 6 },
        { "name": "Pear", "type": "fruit", "value": 3 },
        { "name": "Sweet Potato", "type": "vegetable", "value": 4 },
        { "name": "Oyster", "type": "meat", "value": 4 },
        { "name": "Lamb Chop", "type": "meat", "value": 5 },
        { "name": "Apple", "type": "fruit", "value": 3 },
        { "name": "Beetroot", "type": "vegetable", "value": 2 },
        { "name": "Barley", "type": "grain", "value": 3 },
        { "name": "Fiddlehead Fern", "type": "vegetable", "value": 3 },
        { "name": "Seaweed", "type": "vegetable", "value": 4 },
        { "name": "Goose Egg", "type": "protein", "value": 4 },
        { "name": "Cranberry", "type": "fruit", "value": 2 },
        { "name": "Pumpkin", "type": "vegetable", "value": 4 },
        { "name": "Maple Sap", "type": "sweet", "value": 3 }
    ],
    "condiments": [
        { "name": "Sea Salt", "value": "+1", "target": "meat" },
        { "name": "Olive Oil", "value": "+2", "target": "vegetable" },
        { "name": "Herb Mix", "value": "x2", "target": "meat" },
        { "name": "Balsamic Vinegar", "value": "+1", "target": "fruit" },
        { "name": "Lemon Zest", "value": "+1", "target": "fish" },
        { "name": "Black Pepper", "value": "+2", "target": "protein" },
        { "name": "Cinnamon", "value": "+1", "target": "sweet" },
        { "name": "Ginger", "value": "+2", "target": "meat" },
        { "name": "Butter", "value": "+2", "target": "vegetable" },
        { "name": "Chili Flakes", "value": "+2", "target": "meat" },
        { "name": "Honey Glaze", "value": "+1", "target": "fruit" },
        { "name": "Nutmeg", "value": "+1", "target": "sweet" },
        { "name": "Sesame Oil", "value": "+2", "target": "vegetable" },
        { "name": "Garlic Paste", "value": "x1.5", "target": "meat" },
        { "name": "Smoked Paprika", "value": "+1", "target": "protein" }
    ]
}

class Command(BaseCommand):
    help = 'Loads initial ingredient and condiment data into the database'

    def handle(self, *args, **options):
        # Clear existing data
        Ingredient.objects.all().delete()
        Condiment.objects.all().delete()
        
        # Load ingredients
        for ingredient_data in INITIAL_DATA['ingredients']:
            Ingredient.objects.create(**ingredient_data)
        
        # Load condiments
        for condiment_data in INITIAL_DATA['condiments']:
            Condiment.objects.create(**condiment_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data')) 