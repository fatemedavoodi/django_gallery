from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ContactUsForm



def home(request):
    subject_photo = Subject_photo.objects.all()

    context={
        'subject_photo':subject_photo,
    }
    return render(request,"root/index.html",context=context)



def about(request):
    subject_photo = Subject_photo.objects.all()

    context={
        'subject_photo':subject_photo,
    }
    return render(request,"root/about.html",context=context)



def contact(request):
    if request.method == 'GET':
        subject_photo = Subject_photo.objects.all()
        context={
            'subject_photo':subject_photo,
        }
        return render(request,"root/contact.html",context=context)
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'we recieved your message we call you as soon')
            return redirect('root:contact')
    else:
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')


def services(request):
    services = Services.objects.filter(status=True)
    photographer = Photographer.objects.filter(status=True)
    subject_photo = Subject_photo.objects.all()
    category = Category.objects.all()

    context ={
        'services': services,
        'photo':photographer,
        'subject_photo':subject_photo,
        'category': category,
    }

    return render(request,"root/services.html",context=context)

def gallerysingle(request):
    services = Services.objects.filter(status=True)
    photographer = Photographer.objects.filter(status=True)
    subject_photo = Subject_photo.objects.all()
    category = Category.objects.all()

    context ={
        'services': services,
        'photo':photographer,
        'subject_photo':subject_photo,
        'category': category,
    }
    return render(request,"root/gallery-single.html",context=context)

def gallery(request):
    subject_photo = Subject_photo.objects.all()
    services = Services.objects.filter(status=True)

    context={
        'subject_photo':subject_photo,
        'services':services,
    }
    return render(request,"root/gallery.html",context=context)


