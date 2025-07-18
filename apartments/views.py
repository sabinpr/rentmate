from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Apartment, Tenant
from .serializers import ApartmentSerializer, TenantSerializer
from core.permissions import IsOwnerOrAdmin, IsSelfOrAdmin


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['name']

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'superadmin']:
            return Apartment.objects.all()
        return Apartment.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated, IsSelfOrAdmin]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'apartment__name']
    ordering_fields = ['lease_start', 'lease_end']

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'superadmin']:
            return Tenant.objects.all()
        return Tenant.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        tenant = self.get_object()
        if request.user != tenant.user and request.user.role not in ['admin', 'superadmin']:
            return Response({'detail': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
