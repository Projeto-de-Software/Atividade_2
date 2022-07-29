from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse


def loadPageGrafo(request):
    return render(request, 'views/grafo_form.html', {})




