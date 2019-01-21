from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Timeline, Request, Category, Product, Stock, Answer
from .forms import TimelineForm, RequestForm, AnswerForm

def request_index(request):
    return render(request, 'request.html')


def timeline_index(request):
    form_class = TimelineForm

    # new logic!

    return render(request, 'timeline_index.html', {
        'form': form_class,
    })

def request_index(request):
    form_class = RequestForm

    return render(request, 'request_index.html', {
        'form': form_class,
    })