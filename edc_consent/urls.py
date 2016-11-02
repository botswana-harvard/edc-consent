from django.conf.urls import include, url

from edc_consent.views import HomeView
from edc_consent.admin_site import edc_consent_admin

urlpatterns = [
    url(r'^admin/', include(edc_consent_admin.urls)),
    url(r'^', HomeView.as_view(), name='home-url'),
]
