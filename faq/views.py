from django.shortcuts import render
from .models import Answer

def home(request):
    latest_answer_list = Answer.objects.filter(is_display__exact=1).order_by('-create_date')[:6]
    context = { 'latest_answer_list':latest_answer_list }
    return render(request, 'home.html', context)

def list(request): #미구현
    return render(request, 'home.html', context)

def detail(request, answer_id):
    try:
        answer = Answer.objects.get(pk=answer_id)
    except QueAnswerstion.DoesNotExist:
        raise Http404("Answer does not exist")
    context = { 'answer':answer }
    return render(request, 'detail.html', context)