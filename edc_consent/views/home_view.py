from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_consent.admin_site import edc_consent_admin
from edc_navbar import NavbarViewMixin

from ..site_consents import site_consents


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'edc_consent/home.html'
    navbar_name = 'edc_consent'
    navbar_selected_item = 'consent'

    def __init__(self, *args, **kwargs):
        super(HomeView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            edc_consent_admin=edc_consent_admin,
            consents=site_consents.consents,
        )
        return context
