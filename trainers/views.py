from django.shortcuts import render

from django.http import HttpResponse

from trainers.models import Trainers
from trainers.forms import TrainerForm


def add_trainer(request):
    if request.method == 'GET':
        context = {
            'form': TrainerForm()
        }

        return render(request, 'trainers/add_trainer.html', context=context)

    elif request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            Trainers.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                teaches=form.cleaned_data['teaches'],
                is_free=form.cleaned_data['is_free'],
            )
            context = {
                'message': 'Profesor añadido Correctamente'
            }
            return render(request, 'trainers/add_trainer.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': TrainerForm()
            }
            return render(request, 'trainers/add_trainer.html', context=context)

def list_trainers(request):
    if 'search' in request.GET:
        search = request.GET['search']
        trainers = Trainers.objects.filter(name__icontains=search)
    else:
        trainers = Trainers.objects.all()
    context = {
        'trainers':trainers,
    }
    return render(request, 'trainers/list_trainers.html', context=context)