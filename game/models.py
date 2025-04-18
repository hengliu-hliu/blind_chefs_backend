from django.db import models
from django.utils import timezone

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, default='active')  # active, completed, abandoned
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Game {self.id}: {self.status}"

class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)  # Use ImageField if handling file uploads
    score = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.type})"

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_active_time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Hand(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='hand')
    card = models.ForeignKey(Deck, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name} holds {self.card.card_name}"

class Move_History(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    move_order = models.PositiveIntegerField()

    class Meta:
        ordering = ['move_order']

    def __str__(self):
        return f"{self.player.name} - {self.action} (Order: {self.move_order})"