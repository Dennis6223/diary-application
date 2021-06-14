from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import diaryForm, RegisterUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@csrf_exempt
def home(request):
    context = {}
    return render(request, 'mdiary/index.html', context)

def RegistrationPage(request):
    if request.user.is_authenticated:
        return redirect('editor')
    else:
        form = RegisterUserForm
        if request.method == 'POST':
            form=RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, ' Account for ' + user + '' + ' has been created sucessfully')
                return redirect('login')


    context = {'form':form}
    return render(request, 'mdiary/registration.html', context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('editor')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('editor')
            else:
                messages.info(request, 'Username or Password is incorrect')

        
    context = {}
    return render(request, 'mdiary/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@csrf_exempt
def Editor(request):
    form = diaryForm()
    if request.method == 'POST':
        form = diaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ionize')
    context = {'form' : form}
    return render(request, 'mdiary/editor.html', context)

@login_required(login_url='login')
@csrf_exempt
def Ionize(request):
    diary_entry = Diary.objects.order_by('-diary_time_created')

    context = {'diary_entry':diary_entry}
    return render(request, 'mdiary/ionize.html', context)

def EntryDetail(request, pk_test):
    entry = Diary.objects.get(id=pk_test)
    context = {'entry':entry}
    return render(request, 'mdiary/entry_detail.html', context)

@login_required(login_url='login')
def EditEntry(request, pk):
    entry= Diary.objects.get(id=pk)
    form = diaryForm(instance=entry)
    if request.method == 'POST':
        form= diaryForm(request.POST, instance=entry)
        if form.is_valid:
            form.save()
            return redirect('ionize')

    context = {'form':form}
    return render(request, 'mdiary/update.html', context)

@login_required(login_url='login')
def DeleteEntry(request, pk):
    entry = Diary.objects.get(id=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('ionize')

    context = {'entry':entry}
    return render(request, 'mdiary/delete.html', context)

def TermsOfService(request):
    return render (request, 'mdiary/terms.html')

def PrivacyPolicy(request):
    return render(request, 'mdiary/privacy.html')



