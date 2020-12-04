from .views import ClassView
from django.urls import path

urlpatterns = [
    path( 'api/' , ClassView.as_view() ),
]
