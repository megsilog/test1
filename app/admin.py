from django.contrib import admin
from .models import  Feedback, Event, Resource, Post

# Register each model

admin.site.register(Feedback)
admin.site.register(Event)
admin.site.register(Resource)
admin.site.register(Post)
