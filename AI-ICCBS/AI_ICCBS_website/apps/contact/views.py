from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import ContactForm

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')

    

    GET 