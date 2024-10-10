from django.shortcuts import render, redirect
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def feedBack(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        print(feedBack)
        return redirect('polls:index')
    return redirect('polls:index')


def redirect_polls(request):
    return redirect('polls:index')
