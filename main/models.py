from django.db import models
from django.contrib import messages

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data["title"]) < 2:
            errors["title"] = "Please enter a title of at least 2 characters."
        if len(post_data["network"]) < 2:
            errors["network"] = "Please enter a network of at least 2 characters."
        if len(post_data["description"]) < 5:
            errors["description"] = "Please enter a description of at least 5 characters."
        if len(post_data["release_date"]) < 1:
            errors["release_date"] = "Please enter a release_date of at least 2 characters."

        return errors

class Show(models.Model):
    title = models.CharField(max_length=64)
    network = models.CharField(max_length=64)
    description = models.TextField()
    release_date = models.DateField()