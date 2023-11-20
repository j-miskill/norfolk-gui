import os

from django.shortcuts import render
from django.views import View
from sodapy import Socrata
from pprint import pprint


# Create your views here.


def home_view(request):
    template_name = "trees/home.html"
    context = {}
    return render(request=request, context=context, template_name=template_name)


class TreeView(View):
    template_name = "trees/map.html"
    key = os.environ.get("MAPS_KEY")
    tree_key = os.environ.get("TREE_KEY")
    def get(self, request):
        context = {"key": self.key}
        tree_data = self.get_tree_data(self.tree_key)
        lat_long_data = self.clean_tree_data(tree_data)
        return render(request=request, template_name=self.template_name, context=context)

    def get_tree_data(self, tree_key: str):
        data = {}
        try:
            client = Socrata("data.norfolk.gov", app_token=tree_key)
            data = client.get("jz6u-9g3c", limit=471)
            pprint(data[0])
        except:
            raise Exception("Something went wrong")
        return data

    def clean_tree_data(self, tree_data: dict):
        lat_long_data = {}
        for tree in tree_data:
            name = tree["id"]
            lat = tree["latitude"]
            long = tree["longitude"]
            lat_long_data[name] = {}
            lat_long_data[name]["latitude"] = lat
            lat_long_data[name]["longitude"] = long
        return lat_long_data





