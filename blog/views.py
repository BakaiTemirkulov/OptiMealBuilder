from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from .models import Food, Consume
from django.views import generic
from django.urls import reverse
from .forms import FoodForm

def hello(request):
    return HttpResponse('<h1>Hello World</h1>')

def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'tracker.html', {'foods': foods, 'consumed_food': consumed_food})

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/tracker/')
    return render(request, 'delete.html')

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'products_list.html', {'foods': foods})




class FoodDetailView(generic.DetailView):
    template_name = 'food_detail.html'

    def get_object(self, **kwargs):
        food_id = self.kwargs.get('id')
        return get_object_or_404(models.Food, id=food_id)

class FoodCreateView(generic.CreateView):
    template_name = 'CRUD/food_create.html'
    model = models.Food
    form_class = forms.FoodForm
    success_url = "/food/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(FoodCreateView, self).form_valid(form=form)

class FoodDeleteView(generic.DeleteView):
    template_name = "CRUD/food_delete.html"
    success_url = "/food/"

    def get_object(self, **kwargs):
        food_id = self.kwargs.get("id")
        return get_object_or_404(models.Food, id=food_id)

class FoodUpdateView(generic.UpdateView):
    template_name = "CRUD/food_update.html"
    form_class = forms.FoodForm
    success_url = "/food/"

    def get_object(self, **kwargs):
        food_id = self.kwargs.get("id")
        return get_object_or_404(models.Food, id=food_id)

    def form_valid(self, form):
        return super(FoodUpdateView, self).form_valid(form=form)

def food_search(request):
    query = request.GET.get('q')
    foods = Food.objects.filter(name__icontains=query) if query else Food.objects.all()
    return render(request, 'products_list.html', {'foods': foods})











