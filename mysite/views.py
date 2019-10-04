from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_index(request):
    return HttpResponseRedirect(reverse('market:index'))