from django.test import TestCase, Client
from django.db.models import Max
from .models import gara, calatorie
# Create your tests here.
class testModel(TestCase):
    def setUp(self):
        a1 = gara.objects.create(cod="INS", oras="istambul")
        a2 = gara.objects.create(cod="ord", oras="Oradea")

        calatorie.objects.create(origine=a1, destinatie=a2, durata=100)
        calatorie.objects.create(origine=a1, destinatie=a1, durata=100)
        calatorie.objects.create(origine=a1, destinatie=a2, durata=-100)

    def test_plecari(self):
        a = gara.objects.get(cod="INS")
        self.assertEqual(a.plecari.count(), 3)

    def test_vine(self):
        a = gara.objects.get(cod="INS")
        self.assertEqual(a.vine.count(), 1)

    def test_cal_val(self):
        a1= gara.objects.get(cod="INS")
        a2= gara.objects.get(cod="ord")
        f = calatorie.objects.get(origine=a1, destinatie=a2, durata=100)
        self.assertTrue(f.este_cal_valid())

    def test_cal_inval(self):
        a1= gara.objects.get(cod="INS")
        
        f = calatorie.objects.get(origine=a1, destinatie=a1, durata=100)
        self.assertFalse(f.este_cal_valid())

    def test_cal_val(self):
        a1= gara.objects.get(cod="INS")
        a2= gara.objects.get(cod="ord")
        f = calatorie.objects.get(origine=a1, destinatie=a2, durata=-100)
        self.assertFalse(f.este_cal_valid())

    def test_index(self):
        c = Client()
        rasp = c.get("/")
        self.assertEqual(rasp.status_code, 200)
        self.assertEqual(rasp.context["calatorii"].count(), 2)