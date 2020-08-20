# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

# class IndexTemplateView(LoginRequiredMixin, TemplateView):
class IndexTemplateView(TemplateView):

    # overwrite template to return
    def get_template_names(self):
        template_name = "index.html"
        return template_name

