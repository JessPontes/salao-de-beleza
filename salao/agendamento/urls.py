from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloWorld, name='helloworld'),
    path('', views.agendamentosList, name='agendamentos'),
    path('agendamento/<int:id>', views.agendamentoView, name="agendamento-view"),
    path('newagendamento/', views.newAgendamento, name="new-agendamento"),
    path('edit/<int:id>', views.editAgendamento, name="edit-agendamento"),
    path('changestatus/<int:id>', views.changeStatus, name="change-status"),
    path('delete/<int:id>', views.deleteAgendamento, name="delete-agendamento"),
    path('yourname/<str:name>', views.yourName, name='your-name')
]

