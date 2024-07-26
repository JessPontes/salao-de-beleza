from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    datetime_agendamento = forms.DateTimeField(
        label='Data/Hora',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={
                'type':'datetime-local',
            }),
        input_formats=('%Y-%m-%dT%H:%M',),
    )
    class Meta:
        model = Agendamento
        fields = ('nome', 'services', 'telefone','datetime_agendamento','description', )
    
    def __init__(self, *args, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'