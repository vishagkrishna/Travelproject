from django.http import HttpResponse
from django.shortcuts import render
from . models import items
from . models import values
# Create your views here.
def demo(request):
    obj= items.objects.all()
    val = values.objects.all()
    # return HttpResponse("hello world")
    return  render(request,"index.html",{'result':obj,'final':val})
# def menu(request):
#
#     return render(request, "index.html",)
# # def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse("whatever")