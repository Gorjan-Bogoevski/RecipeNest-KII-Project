from django.db import models

# Create your models here.
from mongoengine import Document, StringField, ListField, IntField, URLField


class Recipe(Document):
    title = StringField(required=True)
    ingredients = ListField(StringField(), required=True)
    steps = ListField(StringField(), required=True)
    cook_time = IntField()
    tags = ListField(StringField())
    image_url = URLField()

    meta = {'collection': 'recipes'}