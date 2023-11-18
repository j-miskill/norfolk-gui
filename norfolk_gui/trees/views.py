import os

from django.shortcuts import render
from django.views import View


# Create your views here.


def home_view(request):
    template_name = "trees/home.html"
    context = {"hello": "hello world"}
    return render(request=request, context=context, template_name=template_name)


class TreeView(View):
    template_name = "trees/map.html"
    key = os.environ.get("MAPS_KEY")
    def get(self, request):
        context = {"key": self.key}
        return render(request=request, template_name=self.template_name, context=context)
