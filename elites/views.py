from django.shortcuts import render, HttpResponse
from .models import Members


# Create your views here.
def index(request):
    return HttpResponse("Hello Elites")


def list_view(request):
    context ={}

    context["dataset"] = Members.objects.all()

    return render(request, "list_view.html", context)


# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Members.objects.get(id=id)

    return render(request, "detail_view.html", context)