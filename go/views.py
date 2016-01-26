from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import forms
import models


def index(request):
    context = {}
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        form = forms.JourneyForm(request.POST)
        if form.is_valid():
            models.journey.objects.create(
                    traveller_name=form.cleaned_data['name'],
                    traveller_email=form.cleaned_data['email'],
                    traveller_phone=form.cleaned_data['phone'],
                    start_time=form.cleaned_data['start_time'],
                    end_time=form.cleaned_data['end_time'])
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Invalid post method !")
    else:
        form = forms.JourneyForm()

    return render(request, 'index.html', {'form': form, })


def query(request):
    if request.method == 'POST':
        return HttpResponse("Post method accepted!")
    else:
        return HttpResponse("God know wtf")
