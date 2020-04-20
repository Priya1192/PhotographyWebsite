from django.shortcuts import render
from .models import Details,Orders
# Create your views here.

def index(request):
    obj = Details.objects.all()
    return render(request,'index.html',{'obj' : obj})

def orders(request):
    obj = Details.objects.all()
    return render(request, 'pgapp/orders.html', {'obj': obj})

def addorder(request):
    if request.method == "POST":

        if request.POST.get('name') and request.POST.get('email') and request.POST.get('city'):
            o = Orders()
            o.name = request.POST["name"]
            o.email = request.POST["email"]
            o.city = request.POST["city"]
            o.event = request.POST["options"]


            o.save()
        else:
            print("incomplete fields")

    return index(request)