from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from records.views import DashboardView, OwnerCreateView, VehicleCreateView, PlateNumberRecognitionView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", DashboardView.as_view(), name="dashboard"),
    path("owner/create/", OwnerCreateView.as_view(), name="owner_create"),
    path("vehicle/create/", VehicleCreateView.as_view(), name="vehicle_create"),
    path("recognition/", PlateNumberRecognitionView.as_view(), name="recognition"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
