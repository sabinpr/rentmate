from rest_framework import serializers
from .models import UtilityBill, RentRecord
from apartments.models import Apartment, Tenant


class UtilityBillSerializer(serializers.ModelSerializer):
    apartment = serializers.PrimaryKeyRelatedField(queryset=Apartment.objects.all())

    class Meta:
        model = UtilityBill
        fields = ['id', 'apartment', 'bill_type', 'amount', 'due_date', 'paid', 'created_at']


class RentRecordSerializer(serializers.ModelSerializer):
    tenant = serializers.PrimaryKeyRelatedField(queryset=Tenant.objects.all())

    class Meta:
        model = RentRecord
        fields = ['id', 'tenant', 'month', 'amount', 'is_paid', 'paid_on']
