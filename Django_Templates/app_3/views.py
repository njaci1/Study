from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'app_3/index.html')

def other(request):
    return render(request,'app_3/other.html')

def relative(request):
    return render(request,'app_3/relative_url.html')
