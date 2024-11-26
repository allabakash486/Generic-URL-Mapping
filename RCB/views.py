from django.shortcuts import render

from django.http import HttpResponse as HR
# Create your views here.

def Virat_Kohli(request):
    return HR('<h1><marquee>Virat is a kind person and loyal person to their team \marquee>  <\h1>')
