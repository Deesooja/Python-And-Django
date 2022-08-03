
# from django import views
from django import views
from django.shortcuts import render, HttpResponseRedirect
from .form import Registrationform
from .models import registration
from django.views import View


# Create your views here.
class ShowData(View):
    def get(self, request):
        fm = Registrationform()
        retrivdata = registration.objects.all()
        return render(request, 'student/show.html', {'form': fm, 'retrivedata_key': retrivdata})


# def show_data(request):
#     fm = Registrationform()
#     retrivdata = registration.objects.all()
#     return render(request, 'student/show.html', {'form': fm, 'retrivedata_key': retrivdata})

class InsertData(View):
    def get(self,request):
     fm = Registrationform()
     retrivdata = registration.objects.all()
     return render(request, 'student/show.html', {'form': fm, 'retrivedata_key': retrivdata})
    
    def post(self, request):
        fm = Registrationform(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            addr = fm.cleaned_data['address']
            datainsert = registration(name=nm, email=em, address=addr)
            datainsert.save()
            fm = Registrationform()
        retrivdata = registration.objects.all()
        return render(request, 'student/show.html', {'form': fm, 'retrivedata_key': retrivdata})




# def insert_data(request):
#     fm = Registrationform()
#     if request.method == 'POST':
#         fm = Registrationform(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['name']
#             em = fm.cleaned_data['email']
#             pw = fm.cleaned_data['password']
#             datainsert = registration(name=nm, email=em, password=pw)
#             datainsert.save()
#             fm = Registrationform()
#         else:
#             fm = Registrationform()
#     retrivdata = registration.objects.all()
#     # return HttpResponseRedirect('/')
#     return render(request, 'student/show.html', {'form': fm, 'retrivedata_key': retrivdata})

class UpdateData(View):
    
    def get(self,request,id):
        data = registration.objects.get(pk=id)
        fm = Registrationform(instance=data)
        return render(request, 'student/updatedata.html', {'form': fm})
    
    def post(self, request,id):
         data = registration.objects.get(pk=id)
         fm = Registrationform(request.POST , instance=data)
         if fm.is_valid():
            fm.save()
         return render(request, 'student/updatedata.html', {'form': fm})
        





# def update_data(request, id):
#     if request.method == 'POST':
#         data = registration.objects.get(pk=id)
#         fm = Registrationform(request.POST, instance=data)
#         if fm.is_valid():
#             fm.save()
#     else:
#         data = registration.objects.get(pk=id)
#         fm = Registrationform(instance=data)
    # retrivdata = registration.objects.all()

    # return render(request, 'student/updatedata.html', {'form': fm})
    # return render(request, 'student/show.html', {'form': fm,'retrivedata_key': retrivdata})

    # return HttpResponseRedirect('/')

class DeleteData(View):
    def get(self,request,id):
        data = registration.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')


# def delete_data(request, id):
#     data = registration.objects.get(pk=id)
#     data.delete()
#     # return render(request, 'student/showdata.html')
#     return HttpResponseRedirect('/')
