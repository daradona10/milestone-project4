from django.shortcuts import render

# Create your views here.
def index(request):
    """A view for the home page"""
    return render(request, "index.html")

