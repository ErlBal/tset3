from django.shortcuts import get_object_or_404

from . import models
from django.views.generic import ListView, DetailView

class ContentView(ListView):
    queryset = models.Content.objects.filter().order_by('-id')
    template_name = 'hashtags/content.html'

    def get_queryset(self):
        return models.Content.objects.filter().order_by('-id')

class ContentDetailView(DetailView):
    template_name = 'hashtags/content_detail.html'

    def get_object(self, **kwargs):
        content_id = self.kwargs.get('id')
        return get_object_or_404(models.Content, id=content_id)

class ContentOaoaoView(ListView):
    queryset = models.Content.objects.filter(tags__name='оаоао')
    template_name = 'hashtags/content_oaoao.html'

    def get_queryset(self):
        return models.Content.objects.filter(tags__name='оаоао')