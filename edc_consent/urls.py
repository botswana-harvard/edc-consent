from django.urls import  path

from .views import HomeView
from .admin_site import edc_consent_admin

app_name = 'edc_consent'

urlpatterns = [
    path('admin/', edc_consent_admin.urls),
    path('', HomeView.as_view(), name='home_url'),
]
