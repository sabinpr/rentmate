from django.contrib import admin
from .models import UtilityBill, RentRecord


@admin.register(UtilityBill)
class UtilityBillAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'bill_type', 'amount', 'due_date', 'paid', 'created_at')
    list_filter = ('bill_type', 'paid', 'due_date')
    search_fields = ('apartment__name',)


@admin.register(RentRecord)
class RentRecordAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'month', 'amount', 'is_paid', 'paid_on')
    list_filter = ('is_paid', 'month')
    search_fields = ('tenant__user__username',)
    ordering = ('-month',)
