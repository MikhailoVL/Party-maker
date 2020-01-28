from django.urls import path

from . import views
from .views import EventList, CreateEvent, EventDetailView

urlpatterns = [
    path('', EventList.as_view(), name='event-list'),
    path('create/', CreateEvent.as_view(), name='create-event'),
    path('detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]