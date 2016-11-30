from serializers import MerchPhotoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from models import MerchPhoto


class MerchPhotoView(viewsets.ModelViewSet):
    merchphoto = MerchPhoto.objects.all()
    serializer_class = MerchPhotoSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    filter_fields =  ('completed',)
    ordering  = ('-date_created',)



