from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
def salomlashish(request):
    return HttpResponse("<h1>Assalomu alaykum</h1>")

def homepage(request):
    return render(request, "home.html")

def kitoblar(request):
    if request.method == 'POST':
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
    soz = request.GET.get("qidirish_sozi")
    natija = Kitob.objects.all()
    if soz:
        natija = natija.filter(nom__contains=soz) or natija.filter(muallif__ism__contains=soz)

    content={
        "kitoblar": natija,
        "forma": KitobForm
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
    if request.method=='POST':
        forma=TalabaForm(request.POST)
        if forma.is_valid():
            data=forma.cleaned_data
            Talaba.objects.create(
                ism=data.get("i"),
                kurs=data.get("k"),
                kitob_soni=data.get("k_s")
            ).save()
        # Talaba.objects.create(
        #     ism=request.POST.get("ism"),
        #     kurs=request.POST.get("kurs"),
        #     kitob_soni=request.POST.get("kitob_soni"),
        # )
        return redirect("/talabalar/")
    soz=request.GET.get("qidirish_sozi")
    natija=Talaba.objects.all()
    if soz:
        natija=natija.filter(ism__contains=soz)

    content = {
        "talabalar": natija,
        "forma": TalabaForm()
    }
    return render(request, "mashq_uchun/Talabalar.html", content)

def mualliflar(request):
    if request.method=='POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            forma.save()
        # Muallif.objects.create(
        #     ism=request.POST.get("ism"),
        #     tugilgan_sana=request.POST.get("t_sana"),
        #     kitoblar_soni=request.POST.get("k_soni"),
        #     tirik=request.POST.get("tirik")
        # ).save()
        return redirect("/mualliflar/")
    content={
        "mualliflar": Muallif.objects.all(),
        "forma": MuallifForm()
    }
    return render(request,"mashq_uchun/Mualliflar.html", content)

def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()

    return redirect('/talabalar/')

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()

    return redirect('/kitoblar/')

def tanlangan_muallif(request, son ):
    content = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request, "mashq_uchun/Muallif.html", content)

def tirik_muallif(request):
    content = {
        "tirik_mualliflar": Muallif.objects.filter(tirik=False)

    }
    return render(request, "mashq_uchun/tirik_mualliflar.html")


def Record(request):
    if request.method == 'POST':
        Record.objects.create(
            ism=request.POST.get("ism"),
            kurs=request.POST.get("kurs"),
            kitob_soni=request.POST.get("kitob_soni"),
        ).save()
        return redirect("/talabalar/")
    soz = request.GET.get("qidirish_sozi")
    natija = Record.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)

    content = {
        "records": natija
    }
    return render(request, "mashq_uchun/Record.html", content)

def talaba_edit(request,pk):
    if request.method=='POST':
        Talaba.objects.filter(id=pk).update(
            kurs=request.POST.get("kurs"),
            kitob_soni=request.POST.get("kitob_soni"),
        )
        return redirect("/talabalar/")
    soz=request.GET.get("qidirish_sozi")
    natija=Talaba.objects.all()
    content={
        "talaba": Talaba.objects.get(id=pk)
    }

    return render(request, 'talaba_edit.html', content)

def kitob_edit(request, pl):
    if request.method=='POST':
        Kitob.objects.filter(id=pl).update(
            janr=request.POST.get("janr"),
            sahifa=request.POST.get("sahifa"),
            muallif=Muallif.objects.get(id =request.POST.get("m")),
        )
        return redirect("/kitoblar/")
    natija=Kitob.objects.all()
    content={
        "kitob": Kitob.objects.get(id=pl),
        "mualliflar": Muallif.objects.all()
    }

    return render(request, 'kitob_edit.html', content)

def muallif_edit(request, pj):
    if request.method=='POST':
        Muallif.objects.filter(id=pj).update(
            ism=request.POST.get("ism"),
            sahifa=request.POST.get("jins"),
            jinsi=request.POST.get("jinsi"),
            tugilgan_sana=request.POST.get("tugilgan_sana"),
            kitoblari_soni=request.POST.get("kitoblari_soni"),
            tirik=request.POST.get("tirik"),
        )
        return redirect("/kitoblar/")
    natija=Kitob.objects.all()
    content={
        "muallif": Kitob.objects.get(id=pj),

    }

    return render(request, 'muallif_edit.html', content)