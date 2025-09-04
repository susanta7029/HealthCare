from django.urls import path
from patients.views import (
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingDetailView,
    PatientDoctorMappingByPatientView
)

urlpatterns = [
    path('', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),   # /api/mappings/
    path('<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),  # /api/mappings/5
    path('patient/<int:patient_id>/', PatientDoctorMappingByPatientView.as_view(), name='mapping-by-patient'),  # /api/mappings/patient/3
]
