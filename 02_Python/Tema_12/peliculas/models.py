from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=25,
                            help_text="Nombre del director",
                            null=False)
    lastname = models.CharField(max_length=35,
                                help_text="Apellido del director",
                                null=False)

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Movie(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Título de la película",
                             null=False)
    running_time = models.IntegerField(null=False,
                                       help_text="Duración en minutos")
    director = models.ForeignKey(Director,
                                 on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.title
