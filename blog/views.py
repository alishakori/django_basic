from django.shortcuts import render
# ?from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . models import Artical





# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_articles'] = Artical.objects.all().order_by("-Created_at")[:9]
        return context
#   def get(self, request, *args,)
  