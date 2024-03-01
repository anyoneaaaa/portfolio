from django.shortcuts import render,HttpResponse

# Create your views here.

def home (request):
    return render (request,"templets\index.html")
    # return (HttpResponse("hello"))

def contact (request):
    return (HttpResponse("contact"))

def about (request):
    return (HttpResponse("about"))



