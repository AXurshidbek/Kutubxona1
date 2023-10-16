from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
def salomlashish(request):
    return HttpResponse("<h1>Assalomu alaykum</h1>")

def homepage(request):
    return render(request, "home.html")

def kitoblar(request):
    soz = request.GET.get("qidirish_sozi")
    natija = Kitob.objects.all()
    if soz:
        natija = natija.filter(nom__contains=soz) or natija.filter(muallif__ism__contains=soz)

    content={
        "kitoblar": natija
    }
    return render(request, "mashq_uchun/kitoblar.html", content)

def Alisher_Navoiy_kitoblari(request):
    content={
        "kitoblar": Kitob.objects.filter(muallif__ism='Alisher Navoiy')
    }
    return render(request, "mashq_uchun/Alisher_Navoiy_kitoblari.html", content)

def kitob(request, son):
    content = {
        "kitob": Kitob.objects.get(id=son)
    }
    return render(request, "mashq_uchun/kitob.html", content)

def talabalar(request):
    soz=request.GET.get("qidirish_sozi")
    natija=Talaba.objects.all()
    if soz:
        natija=natija.filter(ism__contains=soz)

    content = {
        "talabalar": natija
    }
    return render(request, "mashq_uchun/Talabalar.html", content)

def mualliflar(request):
    content={
        "mualliflar": Muallif.objects.all()

    }
    return render(request,"mashq_uchun/Mualliflar.html")

def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()

    return redirect('/talabalar/')

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()

    return redirect('/kitoblar/')