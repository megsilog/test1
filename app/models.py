from django.db import models

class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=10, unique=True)
    topic = models.CharField(max_length=200)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.first_name} {self.last_name} on {self.topic}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    file = models.FileField(upload_to="resources/", null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
