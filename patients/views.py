from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Patient, PatientDoctorMapping
from .serializers import PatientSerializer, PatientDoctorMappingSerializer
import logging

logger = logging.getLogger(__name__)

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(created_by=self.request.user)
        logger.debug(f"Authenticated user: {self.request.user}")
        logger.debug(f"Filtered queryset: {queryset}")
        return queryset

    def perform_update(self, serializer):
        logger.debug(f"Updating patient with data: {serializer.validated_data}")
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        logger.debug(f"Deleting patient: {instance}")
        super().perform_destroy(instance)

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class PatientDoctorMappingDetailView(generics.RetrieveDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorMappingByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)
