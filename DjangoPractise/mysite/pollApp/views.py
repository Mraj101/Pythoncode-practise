from email.policy import HTTP
from urllib import request
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest,HttpResponse
from django.template import loader
# Create your views here.


from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context={
        'latest_question_list':latest_question_list
    }
    return render(request,'pollApp/index.html',context)
# Leave the rest of the views (detail, results, vote) unchanged
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollApp/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)