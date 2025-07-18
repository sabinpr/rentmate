from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apartments.views import ApartmentViewSet, TenantViewSet
from bills.views import UtilityBillViewSet, RentRecordViewSet



from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'apartments', ApartmentViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'bills', UtilityBillViewSet)
router.register(r'rents', RentRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accounts/', include('accounts.urls')),

    # Swagger/OpenAPI docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
