from django.shortcuts import render
from .models import Client
from .forms import ClientForm

def client_form(request):
    form = ClientForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
    ctx = {
        "form": form
    }
    return render(request, "contactform.html", ctx)

def client_list(request):
    clients =Client.objects.all()
    ctx = {
        "clients": clients,
    }
    return render(request, "table.html", ctx)