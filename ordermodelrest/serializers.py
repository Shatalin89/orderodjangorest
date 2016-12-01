from rest_framework import serializers
from .models import MerchPhoto, Merchandise


class MerchPhotoSerializer(serializers.ModelSerializer):
    
    image = serializers.ImageField(max_length=None,use_url=True)
    
    class Meta:
        model =  MerchPhoto
        fields = ('id','idmerch','name','image','created')


class MerchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Merchandise
        fields = ('id', 'name_merch', 'merch_price', 'merch_count', 'merch_enabled', 'merch_del', 'merch_description')
        
