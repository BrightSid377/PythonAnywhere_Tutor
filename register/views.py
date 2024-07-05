from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            uname = form.cleaned_data['username']
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=uname, password=raw_password)
            login(request, user)

            #form.save()
            #get the new user info and set the group for this user to Parent
            #user = User.objects.get(username=uname)
            #parent_group = Group.objects.get(name='Parent')
            #user.groups.add(parent_group)
            #user.save()
            return redirect('login')

        return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
