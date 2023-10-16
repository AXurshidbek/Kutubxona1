from django.db import models

JINS=(
    ('Erkak','Erkak'),
    ('Ayol','Ayol')
)
class Talaba(models.Model):
    ism=models.CharField(max_length=45)
    kurs=models.PositiveSmallIntegerField()
    kitob_soni=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism
class Muallif(models.Model):
    ism=models.CharField(max_length=45)
    jins=models.CharField(max_length=7,choices=JINS)
    tugilgan_sana=models.DateField()
    kitoblar_soni=models.PositiveSmallIntegerField()
    tirik=models.BooleanField()

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom=models.CharField(max_length=101)
    janr=models.CharField(max_length=15)
    sahifa=models.PositiveSmallIntegerField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism=models.CharField(max_length=45)
    ish_vaqti=models.CharField(max_length=15)

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba=models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi=models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana=models.DateField()
    qaytardi=models.BooleanField(default=False)
    qaytarish_sana=models.DateField()

    def __str__(self):
        return self.talaba






