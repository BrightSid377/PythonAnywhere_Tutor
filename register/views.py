from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User,Group

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            form.save()
            #get the new user info and set the group for this user to Parent
            user = User.objects.get(username=uname)
            parent_group = Group.objects.get(name='Parent')
            user.groups.add(parent_group)
            user.save()
            return redirect('login')

        return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
