from django.http.response import HttpResponse
from django.shortcuts import render
from skipass.models import Skipass
from json import dumps, loads
from django.core.serializers import serialize


# Create your views here.
def get_all(request):
    return HttpResponse(serialize('json', Skipass.objects.all()))