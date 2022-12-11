from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas =Pizza.objects.all()

    context= {'all_pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings=Topping.objects.filter(pizza=p)

    context= {'pizza':p, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)

@login_required
def comments(request):
    if request.method == 'POST' and request.POST.get('btn1'):
        form= CommentForm()
        #comment = request.POST.get('comment')
        #Comment.objects.create(pizza_id=pizza_id,username=request.user, text=comment,date_added=date.today())
    #comments = Comment.objects.filter(pizza=pizza_id)
    #pizza = Pizza.objects.get(id=pizza_id)
    else:
        form=CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:index')

    context = {'pizza': pizza, 'comments':comments}

    return render(request, 'pizza/comments.html', context)