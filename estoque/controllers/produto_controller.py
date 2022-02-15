from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from ..models import *
from ..forms import *
from django.core import serializers
from django.contrib import messages
from django.utils.timezone import now
