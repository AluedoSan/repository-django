from django.shortcuts import render, redirect
from django.views import View


# Redirect to index the first page
def redirect_polls(request):
    return redirect('polls:index')


# Class of index
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'polls/index.html')


    def feedBack(self, request, *args, **kwargs):
        if request.method == 'POST':
            feedback = request.POST.get('feedback')
            print(feedback)
            return redirect('polls:index')
        return redirect('polls:index')


# Class of the finance
class FinanceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'polls/finances.html')

