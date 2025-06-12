from django.db import models

# Opciones de posición para jugadores
OPCIONES_POSICION = (
    ('arquero', 'Arquero'),
    ('defensa', 'Defensa'),
    ('mediocampo', 'Mediocampo'),
    ('delantero', 'Delantero'),
)

# Modelo de equipo
class Equipo(models.Model):
    nombre = models.CharField("Nombre del equipo", max_length=50)
    siglas = models.CharField(max_length=10)
    twitter = models.CharField("Cuenta de Twitter", max_length=50)
    campeonatos = models.ManyToManyField('Campeonato', through='CampeonatoEquipo')

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"

# Modelo de jugador
class Jugador(models.Model):
    nombre = models.CharField("Nombre del jugador", max_length=100)
    posicion = models.CharField(max_length=30, choices=OPCIONES_POSICION)
    numero = models.IntegerField("Número en camiseta")
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return f"{self.nombre} - {self.get_posicion_display()} #{self.numero} - {self.equipo.nombre}"

# Modelo de campeonato
class Campeonato(models.Model):
    nombre = models.CharField("Nombre del campeonato", max_length=100)
    patrocinador = models.CharField("Patrocinador", max_length=100)
    equipos = models.ManyToManyField(Equipo, through='CampeonatoEquipo')

    def __str__(self):
        return f"{self.nombre} / {self.patrocinador}"

# Modelo intermedio para relación Equipo <-> Campeonato
class CampeonatoEquipo(models.Model):
    anio = models.IntegerField("Año del campeonato")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="campeonatos_ganados")
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name="equipos_ganadores")
    def __str__(self):
        return f"{self.anio} - {self.equipo.nombre} ganó {self.campeonato.nombre}"
