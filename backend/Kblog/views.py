from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import KblogSerialiser
from .models import Kblog
from .form import searchform
# Create your views here.

@api_view(['GET','POST'])
def get_posts(requests):
    
    pages = Kblog.objects.all()
    serializer = KblogSerialiser(pages, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def index(request):
    return render(request, 'pages/index.html', {
        'form': searchform()
    })

@api_view(['GET'])
def about(request):
    return render(request, 'pages/about.html',{
        'form': searchform()
    })


@api_view(['GET'])
def contact(request):
    return render(request, 'pages/blog.html',{
        'form': searchform()
    })

