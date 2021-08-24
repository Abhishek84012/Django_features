'''CLASS BASED VIEW:- https://ccbv.co.uk/
'''
from django.views.generic import TemplateView


class index(TemplateView):
    template_name = "index.html"
