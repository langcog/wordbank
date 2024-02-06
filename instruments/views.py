from django.shortcuts import render
from django.views.generic import View

from common.models import *
from instruments.models import *


class Stats(View):
    def get(self, request):
        return render(request, "stats.html", {"data": []})
