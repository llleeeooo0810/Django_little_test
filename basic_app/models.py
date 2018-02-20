# from django.db import models
import mongoengine

# Create your models here.
class User(mongoengine.Document):
    first_name = mongoengine.StringField(max_length=128, required=True)
    last_name = mongoengine.StringField(max_length=128, required=True)
    email = mongoengine.EmailField(max_length=128, required=True, unique=True)
