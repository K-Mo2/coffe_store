from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("""
    <ol>
    <li> <a href='/coffe-store/coffe-machines'> Coffe Machines </a> </li>
    <li> <a href='/coffe-store/coffe-pods'> Coffe Pods </a> </li>
    </ol>
    """)

def machines(request):
    return HttpResponse("<h1>Coffe Machines</h1>")

def pods(request):
    return HttpResponse("<h1>Coffe Pods</h1>")