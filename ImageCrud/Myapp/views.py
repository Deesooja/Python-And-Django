from pyexpat.errors import messages
from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from .models import Image

# Create your views here.
# def ShowData(request):
#  if request.method == "POST":
#         prod=Image()
#         prod.photo =request.FILES.get('image')
#         prod.save()
#  img = Image.objects.all()
#  print(img.photo)
#  return render(request, 'myapp/home.html', {'img':img})
class ShowData(View):
    def get(self,request):
        retrivimage = Image.objects.all()
        print(retrivimage)
        return render(request, 'myapp/home.html', {'img': retrivimage})

    def post(self,request):
        if len(request.FILES) !=0:
         prod=Image()
         prod.photo =request.FILES.get('image')
         prod.save()
        return HttpResponseRedirect('/')   

# class InsertData(View):
#     def get(self,request):
#         return render(request,'myapp/addimage.html')

#     def post(self,request):
#         prod=Image()
#         prod.photo =request.FILES.get('image')
#         prod.save()
#         return HttpResponseRedirect('/')