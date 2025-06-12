from django.db import models

# Modelo de equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=10)
    twitter = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"

# Modelo de jugador
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=30)
    numero = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return f"{self.nombre} - {self.posicion} #{self.numero} - {self.equipo.nombre}"

# Modelo de campeonato
class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    patrocinador = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} / {self.patrocinador}"

# Relación de campeonatos ganados por equipos
class CampeonatoEquipo(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="campeonatos_ganados")
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name="ganadores")

    def __str__(self):
        return f"{self.anio} - {self.equipo.nombre} ganó {self.campeonato.nombre}"
