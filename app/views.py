from django.shortcuts import render


# Create your views here.
from app.models import *

def display_topic(request):
    QST=Topic.objects.all()
    d={'topic':QST}
    return render(request,'display_topic.html',d )


def display_webpages(request):
    QSW=Webpages.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_access(request):
    QSA=AccessRecords.objects.all()
    d={'access':QSA}
    return render(request,'display_access.html',d)