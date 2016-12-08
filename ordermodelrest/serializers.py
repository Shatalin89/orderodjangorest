from rest_framework import serializers
from .models import MerchPhoto, Merchandise


class PhotoSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model =  MerchPhoto
        

class MerchPhotoSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model =  MerchPhoto
        fields = ('id','name','image', 'phototype')

class MerchingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Merchandise        


class MerchSerializer(serializers.ModelSerializer):
    photos = MerchPhotoSerializer(many=True)
    class Meta:
        model = Merchandise
        fields = ('id', 'name_merch', 'merch_price', 'merch_count', 'merch_enabled', 'merch_del', 'merch_description', 'photos')

   #  def create(self, validated_data):
   #     photos_data = validated_data.pop('photos')
   #     idmerch = Album.objects.create(**validated_data)
   #     for photos_data in photos_data:
   #         Track.objects.create(album=album, **track_data)
   #     return album
        
