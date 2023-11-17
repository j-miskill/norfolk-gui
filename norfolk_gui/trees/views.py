from django.shortcuts import render

# Create your views here.


def home_view(request):
    template_name = "trees/home.html"
    context = {"hello": "hello world"}
    return render(request=request, context=context, template_name=template_name)
