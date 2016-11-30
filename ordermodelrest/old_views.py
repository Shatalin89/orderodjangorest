from django.shortcuts import render

from models import MerchPhoto
from django.http import Http404

from serializers import MerchPhotoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MerchPhotoList(APIView):

	def get(self, request, format=None):
		merchphoto = MerchPhoto.objects.all()
		serializers = MerchPhotoSerializer(merchphoto, many=True)
		return Response(serializers.data)

	def post(self, request, format=None):
		serializers = MerchPhotoSerializer(data=request.DATA)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data, status=status.HTTP_201_CREATED)
		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		merchphoto = self.get_object(pk)
		merchphoto.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, pk, format=None):
		merchphoto = self.get_object(pk)
		serializer = MerchPhotoSerializer(merchphoto, data=request.DATA)
		if serializer.is_valid:
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    