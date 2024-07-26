from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib import messages
import datetime

@login_required
def agendamentosList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    agendamentosDoneRecently = Agendamento.objects.filter(user=request.user).count()
    
    agendamentosDone = Agendamento.objects.filter(done='done', user=request.user).count()
    agendamentosDoing = Agendamento.objects.filter(done='doing', user=request.user).count()

    if search:
        agendamentos = Agendamento.objects.filter(services__icontains=search, user=request.user)
    elif filter:
        agendamentos = Agendamento.objects.filter(done=filter, user=request.user)
    else:
        agendamentos_list = Agendamento.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(agendamentos_list, 5)
        page = request.GET.get('page')
        agendamentos = paginator.get_page(page)
    
    context = {
        'agendamentos': agendamentos, 
        'agendamentosrecently': agendamentosDoneRecently, 
        'agendamentosdone': agendamentosDone, 
        'agendamentosdoing': agendamentosDoing
    }

    return render(request, 'agendamento/list.html', context)

@login_required
def agendamentoView(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)
    return render(request, 'agendamento/agendamento.html', {'agendamento': agendamento})

@login_required
def newAgendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.done = 'doing'
            agendamento.user = request.user
            agendamento.save()
            return redirect('/')
    else:
        form = AgendamentoForm()
        return render(request, 'agendamento/addagendamento.html', {'form': form})

@login_required
def editAgendamento(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)
    
    if agendamento.done == 'done':
        messages.error(request, 'Este agendamento já foi atendido e não pode ser editado.')
        return redirect('/')

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            agendamento.save()
            messages.success(request, 'Agendamento atualizado com sucesso.')
            return redirect('/')
        else:
            return render(request, 'agendamento/editagendamento.html', {'form': form, 'agendamento': agendamento})
    else:
        form = AgendamentoForm(instance=agendamento)
        return render(request, 'agendamento/editagendamento.html', {'form': form, 'agendamento': agendamento})

@login_required
def deleteAgendamento(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)
    if agendamento.done == 'done':
        messages.error(request, 'Este agendamento já foi atendido e não pode ser deletado.')
        return redirect('/')
    agendamento.delete()
    messages.info(request, 'Agendamento deletado com sucesso.')
    return redirect('/')

@login_required
def changeStatus(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)

    if (agendamento.done == 'doing'):
        agendamento.done = 'done'
    else:
        agendamento.done = 'doing'
    agendamento.save()
    return redirect('/')

def helloWorld(request):
    return HttpResponse('Hello World!')

def yourName(request, name):
    return render(request, 'agendamentos/yourname.html', {'name':name})

