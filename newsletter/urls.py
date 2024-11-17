from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_newsletter, name='newsletter_management'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('unsubscribe/', views.unsubscribe_newsletter, name='unsubscribe_newsletter'),
]
