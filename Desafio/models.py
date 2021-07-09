from django.db import models
from django import forms


class Tecnologias(models.Model):
    nome_Tec = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

    link_Tec = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    descr_Tec = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    tags_Tec = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    objetos = models.Manager()


class InsereTecnologiaForm(forms.ModelForm):
    class Meta:
        # Modelo base
        model = Tecnologias

        # Campos que estarão no form
        fields = [
            'nome_Tec',
            'link_Tec',
            'descr_Tec',
            'tags_Tec'
        ]
