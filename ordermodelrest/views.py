from serializers import MerchPhotoSerializer, MerchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from models import MerchPhoto, Merchandise
from rest_framework import generics

class MerchPhotoView(viewsets.ModelViewSet):
    queryset = MerchPhoto.objects.all()
    serializer_class = MerchPhotoSerializer

class MerchView(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchSerializer

class MerchViewEnabled(generics.ListAPIView):
    #queryset = Merchandise.objects.all()
    serializer_class = MerchSerializer

    def get_queryset(self):
    	merch_enabled = self.kwargs['merch_enabled']
    	return Merchandise.objects.filter(merch_enabled=merch_enabled)


		