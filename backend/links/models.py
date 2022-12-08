from django.db import models


class Link(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Nome do link'
    )
    link = models.CharField(
        max_length=255,
        verbose_name='Endereço de redirecionamento'
    )
    icon = models.CharField(
        max_length=255,
        verbose_name='Classe CSS do ícone'
    )

    show_on_home = models.BooleanField(
        verbose_name='Exibir na landing page'
    )
    order = models.IntegerField(
        null=True,
        verbose_name='Ordem de exibição'
    )

    def __str__(self) -> str:
        return f'Link #{self.pk} - {self.name}'

    class Meta:
        verbose_name_plural = 'links de redirecionamento'
        verbose_name = 'link de redirecionamento'
