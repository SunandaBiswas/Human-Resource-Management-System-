from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/incident/<int:incident_id>/modal/', views.incident_modal, name='incident_modal'),
    path('incident/<int:incident_id>/modal/', views.incident_modal_detail, name='incident_modal_detail'),
    path('incident/<int:incident_id>/modal/', views.incident_detail_modal, name='incident_detail_modal'),
    path('incident/<int:incident_id>/popup/', views.incident_popup_detail, name='incident-popup-detail'),
    path('employee/', include('employee.urls')),  # Register the app's routes here
]

# Serve uploaded files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
