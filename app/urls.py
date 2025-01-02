from django.urls import path
from .views import (
    HomePageView, AboutPageView, 
    FeedbackListView, FeedbackDetailView, FeedbackCreateView,
    EventListView, EventDetailView, EventCreateView,
    ResourceListView, ResourceDetailView,
    PostListView, PostDetailView,
    AdminDashboardView,
    EventEditView, EventDeleteView

)

urlpatterns = [

     path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),

    # Home and About
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    # Feedback URLs
    path('feedbacks/', FeedbackListView.as_view(), name='feedback_list'),
    path('feedbacks/<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedbacks/create/', FeedbackCreateView.as_view(), name='feedback_create'),

    # Event URLs
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    # New routes for editing and deleting
    path('events/<int:pk>/edit/', EventEditView.as_view(), name='event_edit'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    # Resource URLs
    path('resources/', ResourceListView.as_view(), name='resource_list'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
