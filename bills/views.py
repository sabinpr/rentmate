from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend


from .models import UtilityBill, RentRecord
from .serializers import UtilityBillSerializer, RentRecordSerializer
from core.permissions import IsAdminOrReadOnly, IsSelfOrAdmin


class UtilityBillViewSet(viewsets.ModelViewSet):
    queryset = UtilityBill.objects.all()  # <- ADD THIS LINE
    serializer_class = UtilityBillSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['bill_type', 'paid', 'apartment__name']
    ordering_fields = ['due_date', 'amount', 'created_at']
    search_fields = ['apartment__name']

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'superadmin']:
            return UtilityBill.objects.all()
        return UtilityBill.objects.filter(apartment__owner=user)

    def perform_create(self, serializer):
        apartment = serializer.validated_data.get('apartment')
        user = self.request.user
        if user.role not in ['admin', 'superadmin'] and apartment.owner != user:
            raise PermissionDenied("You can only add utility bills for your own apartments.")
        serializer.save()


class RentRecordViewSet(viewsets.ModelViewSet):
    queryset = RentRecord.objects.all()  # <- ADD THIS LINE
    serializer_class = RentRecordSerializer
    permission_classes = [IsAuthenticated, IsSelfOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['tenant__user__username', 'tenant__apartment__name', 'is_paid', 'month']
    ordering_fields = ['month', 'amount', 'paid_on']
    search_fields = ['tenant__user__username']

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'superadmin']:
            return RentRecord.objects.all()
        return RentRecord.objects.filter(tenant__user=user)

    def perform_create(self, serializer):
        tenant = serializer.validated_data.get('tenant')
        user = self.request.user
        if user.role not in ['admin', 'superadmin'] and tenant.user != user:
            raise PermissionDenied("You can only create rent records for yourself.")
        serializer.save()
