from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def register(request):
    """Register as a new user to leave a comment on a Pizza."""
    if request.method != 'POST':
        form =UserCreationForm()
    else:
        form= UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect('pizzas:index')

    context={'form':form}
    return render(request, 'registration/register.html', context)