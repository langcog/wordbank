from django.views.generic import TemplateView
from django.shortcuts import render

class HealthView(TemplateView):
    template_name="health.html"

    def get(self, request):
        return render(request, self.template_name, status=204)