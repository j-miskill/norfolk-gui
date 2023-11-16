from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = {"hello": "hello world"}
    return render(request, context)
