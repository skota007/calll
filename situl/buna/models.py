from django.db import models

# Create your models here.
class gara(models.Model):
    cod = models.CharField(max_length=3)
    oras = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.oras}({self.cod})"  


class calatorie(models.Model):
    origine = models.ForeignKey(gara, on_delete=models.CASCADE, related_name="plecari")
    destinatie = models.ForeignKey(gara, on_delete=models.CASCADE, related_name="vine")
    durata = models.IntegerField()

    def este_cal_valid(self):
        return (self.origine != self.destinatie) and (self.durata>0)

    def __str__(self):
        return f"{self.id} - {self.origine} to {self.destinatie}"

class pasager(models.Model):
    nume = models.CharField(max_length=30)
    prenume = models.CharField(max_length=30)
    CAlatorie = models.ManyToManyField(calatorie,blank=True, related_name="pasageri")

    def __str__(self):
        return f"{self.nume}-{self.prenume}"