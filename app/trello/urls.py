from django.urls import path
from . import views

urlpatterns = [
    path('trello/<str:action>/', views.consume_trello)
]