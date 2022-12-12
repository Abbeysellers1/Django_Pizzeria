from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


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

def comments(request, pizza_id):
    form=CommentForm(data=request.POST)
    comments=Pizza.objects.get(id=pizza_id)
    comments = Comment.objects.all().filter(pizza=pizza_id)
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == 'POST' and request.POST.get('btn1'):
        form= CommentForm()
        comment = request.POST.get('comment')
        Comment.objects.create(pizza_id=pizza_id,username=request.user, text=comment)
    else:
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comments=form.save(commit=False)
            comments.pizza=pizza
            comments.save()
            return redirect('pizzas:index')

    context = {'pizza': pizza, 'form':form, 'comments':comments}

    return render(request, 'pizzas/comments.html', context)
'''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user_id = request.user
            comments.message= comments
            comments.save()
            return redirect('comments', pizza_id=pizza_id)
        else:
            form=CommentForm()
    return render(request, "pizzas/comments.html", {'pizza':pizza, 'form': form})

    template_name = 'pizza_comment.html'
    post = get_object_or_404(Pizza, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment= None

    if request.method == 'POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit= False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request, template_name, {'post':post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
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

    return render(request, 'pizza/comments.html', context)'''