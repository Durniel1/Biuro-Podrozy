from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class SrodekTransportu(models.Model):
    DROGA_PRZEWOZU_CHOICES = {
        "Ld":"Lądowa",
        "Mr":"Morska",
        "Pw":"Powietrzna"
    }
    nazwa = models.CharField(max_length=100)
    typ = models.CharField(max_length=100)
    droga_przewozu = models.TextField(choices=DROGA_PRZEWOZU_CHOICES)
    przewoznik = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Środki Transportu"
    def __str__(self):
        return f'{self.przewoznik} {self.nazwa}'
    def get_absolute_url(self):
        return reverse("SrodekTransportu", args=[self.pk])
class Bilet(models.Model):
    godzina_z = models.DateTimeField(auto_now=True)
    godzina_do = models.DateTimeField(auto_now=True)
    kierunek = models.ForeignKey("Kierunek", on_delete=models.CASCADE)
    #status = models.CharField(max_length=100, default="nieopłacony")
    status = models.BooleanField(default=False)
    nr_siedzenia = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    dodatkowe_oplaty = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    
    class Meta:
        verbose_name_plural = "Bilety"
    def __str__(self):
        return f'z {self.kierunek.z} o {str(self.godzina_z)[:16]} do {self.kierunek.do} o {str(self.godzina_do)[:16]}'
    def get_absolute_url(self):
        return reverse("Bilet", args=[self.pk])
class Kierunek(models.Model):
    z = models.CharField(max_length=100)
    do = models.CharField(max_length=100)
    srodek_transportu = models.ForeignKey("SrodekTransportu", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Kierunki"
    def __str__(self):
        return f'{self.z} -> {self.do}: {self.srodek_transportu.przewoznik} {self.srodek_transportu.nazwa} - droga {self.srodek_transportu.droga_przewozu}'
    def get_absolute_url(self):
        return reverse("Kierunek", args=[self.pk])
class Opinia(models.Model):
    ocena = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    tresc = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Opinie"
    def __str__(self):
        return f'{self.tresc[:10]} {self.ocena}'