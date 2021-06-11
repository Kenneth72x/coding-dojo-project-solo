from django.db import models

# Dream database
class DreamManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #if postData == request.POST
        if len(postData['title']) < 2: 
            errors["title"] = "Title must be at least 2 characters long."
        if len(postData['mood']) < 3:
            errors["mood"] = "Mood must be at least 3 characters long."
        if len(postData['description']) < 10:
            errors["description"] = "Description must be at least 10 characters long."    
        return errors    

class Dream(models.Model):
    title = models.CharField(max_length=255)
    mood = models.CharField(max_length=45)
    dream_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DreamManager()
