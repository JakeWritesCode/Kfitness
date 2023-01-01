from django.shortcuts import render

# Create your views here.
def hello_jake(request):
    response = render(request, "Home.html")
    return response