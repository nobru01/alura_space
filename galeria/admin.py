from django.contrib import admin
from .models import Fotografia

# Register your models here.

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome","legenda","publicada")
    list_display_links = ("id", "nome")
    list_editable= ("publicada",)
    search_fields = ("nome",)       # precisa passar uma tupla como argumento
    list_filter = ("categoria",)    # filtro por categoria
    list_per_page= 10               # Paginação


admin.site.register(Fotografia, ListandoFotografia)
