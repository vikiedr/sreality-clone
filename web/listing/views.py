from django.shortcuts import render
from django.http import HttpResponse
from .models import Flat

# Create your views here.
def list_flats(request):
    flats = Flat.objects.all()
    return render(request, "list_flats.html", {'flats': flats})
    