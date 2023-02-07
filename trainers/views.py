from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
        trainers = Trainers.objects.filter(first_name__icontains=search)
    else:
        trainers = Trainers.objects.all()
    context = {
        'trainers':trainers,
    }
    return render(request, 'trainers/list_trainers.html', context=context)

@login_required
def update_trainer(request, pk):
    trainer = Trainers.objects.get(id=pk) 
    if request.method == 'GET':
        form = TrainerForm(initial = {
            'first_name':trainer.first_name,
            'last_name':trainer.last_name,
            'phone_number':trainer.phone_number,
            'email':trainer.email,
            'teaches':trainer.teaches,
            'is_free':trainer.is_free,
        })
        context ={
            'form':form
        }
        return render(request, 'trainers/update_trainer.html', context=context)

    elif request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():

            my_form = form.cleaned_data

            trainer.first_name = my_form['first_name']
            trainer.last_name = my_form['last_name']
            trainer.phone_number = my_form['phone_number']
            trainer.email = my_form['email']
            trainer.teaches = my_form['teaches']
            trainer.is_free = my_form['is_free']
            trainer.save()
            context = {
                'message': 'Profesor actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': TrainerForm()
            }
        return render(request, 'trainers/update_trainer.html', context=context)

@login_required
def delete_trainer(request, pk):
    trainer = Trainers.objects.get(id=pk)
    if request.method == 'GET':
        form = TrainerForm(initial = {
            'first_name':trainer.first_name,
            'last_name':trainer.last_name,
            'phone_number':trainer.phone_number,
            'email':trainer.email,
            'teaches':trainer.teaches,
            'is_free':trainer.is_free,
        })
        context ={
            'form':form
        }
        return render(request, 'trainers/delete_trainer.html', context=context)

    elif request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            trainer = Trainers.objects.get(id=pk)
            trainer.delete()
            context = {
                'message': 'Profersor/ra borrado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': TrainerForm()
            }
        return render(request, 'trainers/delete_trainer.html', context=context)