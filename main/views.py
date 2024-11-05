from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class HelloView(TemplateView):
    template_name = "hello.html"


class ByeView(TemplateView):
    template_name = "bye.html"