from django.contrib import admin
from RegistroPokemon.models import pokemon


# Register your models here.
class registroAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre','elemento','genero','estado')
admin.site.register(pokemon,registroAdmin)
