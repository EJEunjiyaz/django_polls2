from django.shortcuts import render

from .models import Item, Choice

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    #context = {'Items': Item.objects.all()}
    #return render(request, 'market/index.html', context)
    # return HttpResponse('my_mind_smile_dekkapok')
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'market/index.html', context)

def result(request, item_id):
    choice_list = Choice.objects.filter(item_id=item_id)
    context = {'choice_list': choice_list}
    return render(request, 'market/results.html', context)
