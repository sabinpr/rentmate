from django.db import models
from django.utils import timezone
from apartments.models import Apartment, Tenant


class UtilityBill(models.Model):
    BILL_TYPES = [
        ('electricity', 'Electricity'),
        ('water', 'Water'),
        ('internet', 'Internet'),
        ('other', 'Other'),
    ]

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='utility_bills')
    bill_type = models.CharField(max_length=20, choices=BILL_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_overdue(self):
        return not self.paid and self.due_date < timezone.now().date()

    def __str__(self):
        return f"{self.bill_type.title()} Bill for {self.apartment.name}"


class RentRecord(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='rent_records')
    month = models.DateField()  # First day of the month
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_on = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('tenant', 'month')

    def __str__(self):
        return f"{self.tenant.user.get_full_name()} - {self.month.strftime('%B %Y')}"
