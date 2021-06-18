from django.shortcuts import render

# Create your views here.
def index(request,room=1000,team="keer"):
    return render(request,"frontend/index.html")