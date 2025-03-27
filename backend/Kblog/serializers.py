from rest_framework import serializers
from .models import Kblog

class KblogSerialiser(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Kblog
        fields = ['id', 'title','body', 'image','image_url']
        
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None 