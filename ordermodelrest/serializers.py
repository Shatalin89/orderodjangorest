from rest_framework import serializers
from .models import MerchPhoto


class MerchPhotoSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None,use_url=True)
    
    class Meta:
        model =  MerchPhoto
        fields = ('id','idmerch','name','image','created')