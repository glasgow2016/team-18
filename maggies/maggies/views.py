from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

@login_required
def home(request):
    return render(request, "home.html")

def login_page(request):
    if request.method == "POST":
        if "username" in request.POST and "password" in request.POST:
            user = authenticate(username=request.POST["username"],
                                password=request.POST["password"])
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect(request.POST.get('next', '/'))
            else:
                # No backend authenticated the credentials
                context = {"showError": True, "message": "Login details are incorrect."}
                return render(request, "login.html", context)
        else:
            print("check failed")
    print("Falling back to basic page")
    return render(request, "login.html")

def data_form(request):
    return render(request, "data-form.html")
