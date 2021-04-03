from django.views.generic import TemplateView

class HealthView(TemplateView):
    template_name="health.html"