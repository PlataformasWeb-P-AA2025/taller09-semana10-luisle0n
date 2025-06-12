from django.contrib import admin

# Importar modelos personalizados
from .models import Equipo, Jugador, Campeonato, CampeonatoEquipo

# Personalización del modelo Jugador
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'numero', 'salario', 'get_equipo')
    search_fields = ('nombre', 'posicion', 'equipo__nombre')

    def get_equipo(self, obj):
        return obj.equipo.nombre
    get_equipo.short_description = 'Equipo'

# Personalización del modelo Equipo
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'twitter')
    search_fields = ('nombre', 'siglas')

# Personalización del modelo Campeonato
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'patrocinador')
    search_fields = ('nombre', 'patrocinador')

# Personalización del modelo CampeonatoEquipo
class CampeonatoEquipoAdmin(admin.ModelAdmin):
    list_display = ('anio', 'get_equipo', 'get_campeonato')
    search_fields = ('equipo__nombre', 'campeonato__nombre')

    def get_equipo(self, obj):
        return obj.equipo.nombre
    get_equipo.short_description = 'Equipo'

    def get_campeonato(self, obj):
        return obj.campeonato.nombre
    get_campeonato.short_description = 'Campeonato'

# Registro de modelos con sus clases admin
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CampeonatoEquipo, CampeonatoEquipoAdmin)
