from django.urls import path
from .views import get_posts, index

urlpatterns = [
    path('api/pages/', get_posts, name='get_posts'),
    path('index/', index, name='index'),
]
