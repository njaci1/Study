from django.shortcuts import render
from django.http import HttpResponse
from app_2.models import USERS
from app_2.forms import NewUserForm

# Create your views here.
def index(request):
    return HttpResponse('User Created Successfully')

def callback(request):
    return HttpResponse('a different view')

def templates(request):
    return render(request,"app_2/index.html")

def exercise(request):
    items = USERS.objects.all()
    context = {"records":items}
    return render(request, "app_2/exercise.html",context)

def newUser(request):
    #this function displays form on browser for user to fill in and submits the
    #to the database

    form = NewUserForm() #instantiates the form class in the forms.py

    if request.method == 'POST': #this line is called when the user clicks submit button on the form
        form = NewUserForm(request.POST) #the class in formss.py is instantiated again with a filled in form
        if form.is_valid(): #form is validated
            form.save(commit=True) #from inputs aree saved and commited to the Database
            return users(request) # in this case i was calling the users view to display the names in the database
        else:
            print('Form Invalid')

    return render(request, "app_2/ModelForm.html",{'form':form}) # this line is called to display the form on browser. it uses the ModelForm template

def users(request):
    user = USERS.objects.all()
    context = {"USERS":user}
    return render(request, "app_2/users.html",context)
