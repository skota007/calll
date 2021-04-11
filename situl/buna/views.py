from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import calatorie, gara, pasager

# Create your views here.
def index(request):
    context= {
        "calatorii": calatorie.objects.all()
    }
    return render(request, "buna/index.html", context)

def cal(request, cal_id):
    try:
        cal = calatorie.objects.get(pk=cal_id)
    except calatorie.DoesNotExist:
        raise Http404("nu exista")

    context = {
        "cal": cal,
        "pas":cal.pasageri.all(),
        "non_pasageri":pasager.objects.exclude(CAlatorie=cal).all()
    }

    return render(request, "buna/rasp.html",context)

def book(request, cal_id):
    try:
        pasager_id = int(request.POST["pasageri"])
        pasa = pasager.objects.get(pk=pasager_id)
        cal = calatorie.objects.get(pk=cal_id)
    except pasa.DoesNotExist:
        return render(request, "buna/eroare.html", {"mesaj":"fara pasager"})
    except calatorie.DoesNotExist:
        return render(request, "buna/eroare.html", {"mesaj":"fara calatorie"})    
    except KeyError:
        return render(request, "buna/eroare.html", {"mesaj":"fara selectie"})

    pasa.CAlatorie.add(cal)
    return HttpResponseRedirect(reverse("cal" , args=(cal_id,)))