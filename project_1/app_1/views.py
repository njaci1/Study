from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import AccessRecord, Webpage, Topics
from app_1.forms import BasicForm


# Create your views here.
def index(request):
    #my_dict = {'insert_me':'views.py file'}
    return render(request,'app_1/index.html')

def page2(request):
    weblist = AccessRecord.objects.all()
    context = {'accessed_records':weblist}
    return render(request, 'app_1/page2.html', context)

def FormView(request):
    form = BasicForm()
    form_dict= {'form':form}
    return render(request,'app_1/BasicForm.html',context=form_dict)
