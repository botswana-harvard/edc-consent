from edc_base.views import EdcBaseViewMixin
from django.views.generic.base import TemplateView
from edc_consent.admin import edc_consent_admin


class HomeView(EdcBaseViewMixin, TemplateView):

    template_name = 'edc_consent/home.html'

    def __init__(self, *args, **kwargs):
        super(HomeView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            edc_consent_admin=edc_consent_admin,
            #consents=consents,
            #consent_versions=consent_versions,
            #current_consent_versions=current_consent_versions,
        )
        return context

    def consent_versions(self):
        return NOne