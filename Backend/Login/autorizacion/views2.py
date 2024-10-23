from django.views.generic import TemplateView
from django.conf import settings
import os

class AngularView(TemplateView):
    template_name = 'index.html'  # El archivo que deseas mostrar

    def get_template_names(self):
        return [os.path.join(settings.STATICFILES_DIRS[0], 'index.html')]
