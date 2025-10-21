from django.shortcuts import render , redirect
from .forms import SendMessageForm
from .models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, 'portefolio/index.html')


def send_messagepage(request):
    msg = None
    if request.method =='POST':
        form =SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Message envoye avec succes!"
            form = SendMessageForm()
    else:
        form = SendMessageForm()
    context = { 'form': form, 'msg': msg}
    return render(request, 'portefolio/send_message.html', context)

@login_required
def messagepage(request):
    message = Message.objects.all()
    context= {'msg': message}
    return render(request, 'portefolio/message.html', context)

def loginpage(request):
    if request.method =='POST':
        form =AuthenticationForm(request, data =  request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request, 'portefolio/message.html')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'registration/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('index')