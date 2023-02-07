from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.http import HttpResponse
from plans.models import Plans
from plans.forms import PlanForm

def add_plan(request):
    if request.method == 'GET':
        context = {
            'form': PlanForm()
        }

        return render(request, 'plans/add_plan.html', context=context)

    elif request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            Plans.objects.create(
                name=form.cleaned_data['name'],
                detail=form.cleaned_data['detail'],
                cost=form.cleaned_data['cost'],
            )
            context = {
                'message': 'Plan añadido Correctamente'
            }
            return render(request, 'plans/add_plan.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': PlanForm()
            }
            return render(request, 'plans/add_plan.html', context=context)

def list_plans(request):
    if 'search' in request.GET:
        search = request.GET['search']
        plans = Plans.objects.filter(name__icontains=search)
    else:
        plans = Plans.objects.all()
    context = {
        'plans':plans,
    }
    return render(request, 'plans/list_plans.html', context=context)

@login_required
def update_plan(request, pk):
    plan = Plans.objects.get(id=pk)
    
    if request.method == 'GET':
        form = PlanForm(initial = {
            'name':plan.name,
            'detail':plan.detail,
            'cost':plan.cost,
        })
        context ={
            'form':form
        }
        return render(request, 'plans/update_plan.html', context=context)

    elif request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan.name = form.cleaned_data['name']
            plan.detail = form.cleaned_data['detail']
            plan.cost = form.cleaned_data['cost']
            plan.save()

            context = {
                'message': 'Plan actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PlanForm()
            }
        return render(request, 'plans/update_plan.html', context=context)

@login_required
def delete_plan(request, pk):
    plan = Plans.objects.get(id=pk)
    if request.method == 'GET':
        form = PlanForm(initial = {
            'name':plan.name,
            'detail':plan.detail,
            'cost':plan.cost,
        })
        context ={
            'form':form
        }
        return render(request, 'plans/delete_plan.html', context=context)

    elif request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = Plans.objects.get(id=pk)
            plan.delete()
            context = {
                'message': 'Plan borrado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': PlanForm()
            }
        return render(request, 'plans/delete_plan.html', context=context)