from django.shortcuts import render
from .models import Qusetion , Answer
from .forms import AnswerForms
# Create your views here.


def qusetions_list(request):
    data = Qusetion.objects.all()
    return render(request,'forum/list.html',{'data':data})



def qusetions_detail(request, id):
    question = Qusetion.objects.get(id=id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForms(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.question = question
            myform.save()
            form = AnswerForms()
    else:
        form = AnswerForms()
    return render(request, 'forum/detail.html', {'question': question,'answers':answers,'form':form})
