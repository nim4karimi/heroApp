from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'thugh/index.html'


class AboutPageView(TemplateView):
    template_name = 'thugh/about.html'