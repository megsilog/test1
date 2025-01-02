from django.shortcuts import render
from django.views.generic import TemplateView

class AdminDashboardView(TemplateView):
    template_name = 'app/admin_dashboard.html'
class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Feedback, Event, Resource, Post


# Feedback Views
class FeedbackListView(ListView):
    model = Feedback
    template_name = "app/feedback_list.html"
    context_object_name = "feedbacks"

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = "app/feedback_detail.html"
    context_object_name = "feedback"

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['student', 'topic', 'feedback_text']
    template_name = "app/feedback_form.html"
    success_url = reverse_lazy('feedback_list')

from .forms import EventForm
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event

# Event Views
class EventListView(ListView):
    model = Event
    template_name = "app/event_list.html"
    context_object_name = "events"

class EventDetailView(DetailView):
    model = Event
    template_name = "app/event_detail.html"
    context_object_name = "event"

class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'event_date', 'location']
    template_name = "app/event_form.html"
    success_url = reverse_lazy('admin_dashboard')

class AdminDashboardView(ListView):
    model = Event
    template_name = "app/admin_event_list.html"
    context_object_name = "events"

# Event Edit View
class EventEditView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "app/admin_event_form.html"
    success_url = reverse_lazy('admin_dashboard')  # Redirect to the create page with list below

# Event Delete View
class EventDeleteView(DeleteView):
    model = Event
    template_name = "app/event_confirm_delete.html"
    success_url = reverse_lazy('admin_dashboard') 


# Resource Views
class ResourceListView(ListView):
    model = Resource
    template_name = "app/resource_list.html"
    context_object_name = "resources"

class ResourceDetailView(DetailView):
    model = Resource
    template_name = "app/resource_detail.html"
    context_object_name = "resource"

# Post Views
class PostListView(ListView):
    model = Post
    template_name = "app/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "app/post_detail.html"
    context_object_name = "post"
