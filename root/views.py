from django.shortcuts import render

def home(request):
    return render(request,"root/index.html")

def about(request):
    return render(request,"root/about.html")

def contact(request):
    return render(request,"root/contact.html")

def services(request):
    return render(request,"root/services.html")

def gallery(request):
    return render(request,"root/gallery.html")

def gallery_single(request):
    return render(request,"root/gallery-single.html")

