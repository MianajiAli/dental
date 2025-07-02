
from rest_framework import viewsets, permissions
from .serializers import AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Appointment
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['doctor', 'date']
    ordering_fields = ['date', 'time']
    search_fields = ['description']

    def perform_create(self, serializer):
        if self.request.user.role == 'patient':
            serializer.save(patient=self.request.user)
        else:
            serializer.save()
