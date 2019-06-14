from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.contrib.auth import user_logged_in

from .models import Note, LocationLog


class EntryView(generic.TemplateView):
    template_name = 'notes/entry.html'


def submit(request):
    print()
    note = Note(user=request.user.username, text=request.POST['text'], date=timezone.now())
    note.save()
    return HttpResponseRedirect(reverse('home'))


# Create your views here.
