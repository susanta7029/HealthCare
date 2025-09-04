from django.urls import path
from .views import (
    PatientListCreateView,
    PatientDetailView,
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingDetailView,
    PatientDoctorMappingByPatientView
)

urlpatterns = [
    path('', PatientListCreateView.as_view(), name='patient-list-create'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # 👇 keep this before <int:pk>
    path('mappings/patient/<int:patient_id>/', PatientDoctorMappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
]