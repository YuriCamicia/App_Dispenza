from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Prodotto_Dispensa(models.Model):
    quantità = models.PositiveSmallIntegerField(help_text='quantità prodotto')
    scadenza = models.DateField(help_text='gg/mm/aa')
    #prezzo = models.DecimalField(max_digits=5, decimal_places=2,help_text='prezzo prodotto',validators=[MinValueValidator(0.01)])
    nome = models.CharField(max_length=32, help_text='nome prodotto',blank=False)

class Prodotto_Spesa(models.Model):
    quantità = models.PositiveSmallIntegerField(help_text='quantità prodotto')
    prezzo = models.DecimalField(max_digits=5, decimal_places=2, help_text='prezzo prodotto',
                                 validators=[MinValueValidator(0.01)])
    nome = models.CharField(max_length=32, help_text='nome prodotto',blank=False)

    def calc_prezzo(self):
        total = 0
        #all_product =Spesa.objects.filter(prodotto=self)
        #for prodotto in all_product:
        total += self.prezzo * self.quantità
        return total


class Spesa(models.Model):
    titolo = models.CharField(max_length=32,help_text='Nome spesa')
    prezzo_tot = models.DecimalField(max_digits=6, decimal_places=2,help_text='prezzo spesa',
                                     validators=[MinValueValidator(0.01)], blank=True)
    #prodotto = models.ForeignKey('Prodotto_Spesa', on_delete=models.PROTECT)

    prodotto = models.ManyToManyField(Prodotto_Spesa)

    #def calc_prezzo(self):
    #    total = 0
    #    all_product =self.prodotto.objects.all()
    #    for prodotto in all_product:
    #        total += prodotto.prezzo * prodotto.quantità

    #   return total

    #class Meta:
        #unique_together = ( ('prodotto','prezzo_tot'), )
        #index_together  = ( ('prodotto','prezzo_tot'), )