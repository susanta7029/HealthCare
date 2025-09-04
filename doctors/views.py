from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer
import logging

logger = logging.getLogger(__name__)

# Create your views here.

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.debug(f"Creating doctor with data: {serializer.validated_data}")
        serializer.save()
        logger.debug("Doctor created successfully.")

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
