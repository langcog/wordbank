from django.views.generic import TemplateView
from django.http import HttpResponse

class HealthView(TemplateView):
    template_name="health.html"

    def get(self, request):
        return HttpResponse(status=204)