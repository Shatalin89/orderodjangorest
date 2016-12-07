from rest_framework import serializers
from .models import MerchPhoto, Merchandise


class MerchPhotoSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model =  MerchPhoto
        fields = ('id','name','image', 'phototype')


class MerchSerializer(serializers.ModelSerializer):
    photos = MerchPhotoSerializer(many=True)
    class Meta:
        model = Merchandise
        fields = ('id', 'name_merch', 'merch_price', 'merch_count', 'merch_enabled', 'merch_del', 'merch_description', 'photos')
        
