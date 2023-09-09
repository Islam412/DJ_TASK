from django.shortcuts import render
from .models import Qusetion , Answer

# Create your views here.


def qusetions_list(request):
    data = Qusetion.objects.all()
    return render(request,'forum/list.html',{'data':data})



def qusetions_detail(request, id):
    question = Qusetion.objects.get(id=id)
    answers = Answer.objects.filter(qusetion=question)
    return render(request, 'forum/detail.html', {'question': question,'answers':answers})
