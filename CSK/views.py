from django.shortcuts import render

from django.http import HttpResponse as HR
# Create your views here.

def Jaddu(request):
    return HR('<h1><marquee>Jaddu bhai is Best player \marquee>  <\h1>')
