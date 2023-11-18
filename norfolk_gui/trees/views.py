from django.shortcuts import render
from django.views import View


# Create your views here.


def home_view(request):
    template_name = "trees/home.html"
    context = {"hello": "hello world"}
    return render(request=request, context=context, template_name=template_name)


class TreeView(View):
    template_name = "trees/map.html"

    def get(self, request):
        return render(request, self.template_name)
