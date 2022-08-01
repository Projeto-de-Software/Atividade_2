from django.db import models
from django.utils import timezone

class PlotImageGrafo(models.Model):
    imagePlot = models.ImageField(upload_to='images/')
    imagePlotBusca = models.ImageField(upload_to='images/')
