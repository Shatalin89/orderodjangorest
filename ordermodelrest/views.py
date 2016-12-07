from serializers import MerchPhotoSerializer, MerchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from models import MerchPhoto, Merchandise


class MerchPhotoView(viewsets.ModelViewSet):
    queryset = MerchPhoto.objects.all()
    serializer_class = MerchPhotoSerializer

class MerchView(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchSerializer


		