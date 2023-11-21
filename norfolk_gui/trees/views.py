import os

from django.shortcuts import render
from django.views import View
from sodapy import Socrata
from pprint import pprint
import json
import requests


# Create your views here.


def home_view(request):
    template_name = "trees/home.html"
    context = {}
    context['intro'] = get_intro()
    return render(request=request, context=context, template_name=template_name)

def get_intro():
    print(os.listdir("trees"))
    f = open("trees/intro.txt", "r")
    lines = f.readlines()
    f.close()
    return lines


class TreeView(View):
    template_name = "trees/map.html"
    key = os.environ.get("MAPS_KEY")
    tree_key = os.environ.get("TREE_KEY")

    def get(self, request):
        context = {"key": self.key}
        tree_data = self.get_tree_data()
        final_data = self.clean_tree_data(tree_data.json())
        context["data"] = {}
        context['data'] = json.dumps(final_data)
        return render(request=request, template_name=self.template_name, context=context)



    def get_tree_data(self):
        data = {}
        data = requests.get("https://data.norfolk.gov/resource/jz6u-9g3c.json")
        return data

    def clean_tree_data(self, tree_data):
        data = {}
        for tree in tree_data:
            id = tree['id']
            data[id] = {"latitude": "",
                        "longitude": "",
                        "species": "",
                        "genus": "",
                        "common_name": "",
                        "id": id}
            data[id]['latitude'] = tree['latitude']
            data[id]['longitude'] = tree['longitude']

            try:
                data[id]['species'] = tree['species']
            except:
                data[id]['species'] = "No species"

            try:
                data[id]['genus'] = tree['genus']
            except:
                data[id]['genus'] = "No genus"

            try:
                data[id]['common_name'] = tree['common_name']
            except:
                data[id]['common_name'] = "No common name"

            # need latitude, longitude, id, species, genus

        return data





