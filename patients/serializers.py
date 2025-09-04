from rest_framework import serializers
from .models import Patient, PatientDoctorMapping
from doctors.models import Doctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor']  # include id

    def validate(self, data):
        # Ensure patient and doctor IDs are provided
        if 'patient' not in data or 'doctor' not in data:
            raise serializers.ValidationError("Both 'patient' and 'doctor' fields are required.")

        return data