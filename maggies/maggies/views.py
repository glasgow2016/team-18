from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import VisitorForm

@login_required
def home(request):
    if request.method=="POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            print("Form is valid.")
            return render(request, "home.html")
        else:
            print("Form is not valid.")

    form = VisitorForm()
    return render(request, "home.html", {"form": form})


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

@login_required
def logout_page(request):
    logout(request)
    return redirect('/')

@login_required
def reports(request):
    return render(request, "reports.html")

@login_required
def recent(request):
    return render(request, "recent.html")

@login_required
def activities(request):
    return render(request, "activities.html")
