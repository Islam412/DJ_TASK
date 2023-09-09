from django.shortcuts import render
from .models import Qusetion , Answer

# Create your views here.


def qusetions_list(request):
    data = Qusetion.objects.all()
    return render(request,'forum/list.html',{'data':data})