from django.urls import path
from .views import get_posts, index,  about, contact

urlpatterns = [
    path('api/pages/', get_posts, name='get_posts'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', contact, name='contact')
]
