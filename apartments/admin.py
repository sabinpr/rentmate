from django.contrib import admin
from .models import Apartment, Tenant


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name', 'address', 'owner__username')
    list_filter = ('owner',)


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('user', 'apartment', 'lease_start', 'lease_end', 'rent_amount')
    search_fields = ('user__username', 'apartment__name')
    list_filter = ('lease_start', 'lease_end')
