from django.db import models
from django.contrib.auth import get_user_model


class Agendamento(models.Model):

    STATUS = (
        ('doing', 'doing'),
        ('done', 'done'),
    )

    SERVICES = (
        ('Corte', 'Corte: R$ 50 - R$ 200'),
        ('Coloração', 'Tintura Completa: R$ 100 - R$ 400'),
        ('Mexas/Reflexos', 'Mechas/Reflexos: R$ 150 - R$ 600'),
        ('Hidratação', 'Hidratação: R$ 50 - R$ 150'),
        ('Botox', 'Botox Capilar: R$ 200 - R$ 500'),
        ('Escova', 'Escova Simples: R$ 30 - R$ 80'),
        ('Progressiva', 'Escova Progressiva: R$ 200 - R$ 800')
    )

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    datetime_agendamento = models.DateTimeField('data/hora', null=True, blank=True)
    description = models.TextField('descrição')
    services = models.CharField('serviço',
        max_length=50,
        choices=SERVICES,
    )
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.services
