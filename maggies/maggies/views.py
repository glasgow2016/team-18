from django.shortcuts import render


def login(request):
    return render(request, "login.html")

def data_form(request):
    return render(request, "data-form.html")
