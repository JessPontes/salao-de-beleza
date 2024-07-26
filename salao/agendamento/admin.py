from django.contrib import admin
from django.db.models import Count
from datetime import datetime, timedelta
from .models import Agendamento

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'datetime_agendamento', 'services', 'done', 'user')
    list_filter = ('done', 'services')
    search_fields = ('nome', 'telefone', 'services')

    def desempenho_semanal(self, request):
    
        uma_semana_atras = datetime.now() - timedelta(days=7)
        
        agendamentos_semanais = Agendamento.objects.filter(
            done='done', 
            updated_at__gte=uma_semana_atras
        ).count()

        return f"Agendamentos concluídos na última semana: {agendamentos_semanais}"

admin.site.register(Agendamento, AgendamentoAdmin)
