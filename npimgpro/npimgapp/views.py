from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, "npimgapp/index.html", context)
    # template = loader.get_template("npimgapp/index.html")
    # return HttpResponse(template.render())
