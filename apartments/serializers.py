from rest_framework import serializers
from .models import Apartment, Tenant
from django.contrib.auth import get_user_model

User = get_user_model()


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['id', 'name', 'address', 'owner']


class TenantSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    apartment = serializers.PrimaryKeyRelatedField(queryset=Apartment.objects.all())

    class Meta:
        model = Tenant
        fields = ['id', 'user', 'apartment', 'lease_start', 'lease_end', 'rent_amount']
