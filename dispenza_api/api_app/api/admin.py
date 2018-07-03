from django.contrib import admin

from api_app.api.models import Prodotto_Dispensa, Spesa, Prodotto_Spesa


@admin.register(Prodotto_Dispensa)
class ProdottiDispensaAdmin(admin.ModelAdmin):
    fields = ('nome','scadenza','quantità')
    list_display = ['nome','scadenza','quantità']
    search_fields = ('nome','scadenza','quantità')

@admin.register(Prodotto_Spesa)
class ProdottiDispensaAdmin(admin.ModelAdmin):
    fields = ('nome','prezzo','quantità')
    list_display = ['nome','prezzo','quantità']
    search_fields = ('nome','prezzo','quantità')


@admin.register(Spesa)
class SpesaAdmin(admin.ModelAdmin):
    fields = ('titolo','prodotto','prezzo_tot')
    ##list_display = ['titolo','prodotto','prezzo_tot']
    search_fields = ('titolo','prodotto','prezzo_tot')