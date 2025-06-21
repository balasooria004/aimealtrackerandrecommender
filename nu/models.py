from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField  # For Postgres
# For SQLite, use models.JSONField (Django 3.1+)

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_weight = models.FloatField()
    target_weight = models.FloatField()
    height = models.FloatField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    activity_level = models.CharField(max_length=50)
    goal = models.CharField(max_length=50)
    daily_targets = models.JSONField(default=dict, blank=True, null=True)
    calorie_split = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class MealLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=5000)
    food = models.CharField(max_length=5000)
    quantity = models.CharField(max_length=50)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField()  # For daily grouping

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} - {self.food} ({self.date})"
