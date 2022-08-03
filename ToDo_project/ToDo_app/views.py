from turtle import done
from django.shortcuts import render,HttpResponseRedirect
from .form import All_todo_form
from .models import All_todo,Done_todo,History_todo
# Create your views here.

def todo_showadd(request):
    if request.method == 'POST':
        fm = All_todo_form(request.POST)
        if fm.is_valid():
            todo = fm.cleaned_data['todo']
            save_todo = All_todo(todo=todo)
            save_todo_history = History_todo(todo=todo)
            save_todo_history.save()
            save_todo.save()
        fm = All_todo_form()

    else:
        fm = All_todo_form()
    All_todo_retrive = All_todo.objects.all()
    retrive_done_data = Done_todo.objects.all()
    return render(request,'ToDo_app/home.html',{'form':fm,'retrive_data':All_todo_retrive, 'done_data':retrive_done_data})

def todo_done(request ,id):
    todo_data = All_todo.objects.get(pk=id)
    done_data = todo_data.todo
    save_done_data= Done_todo(todo = done_data)
    save_todo_history = History_todo(pk=id,todo = done_data,status='done')
    save_todo_history.save()
    save_done_data.save()
    todo_data.delete()
    retrive_done_data = Done_todo.objects.all()
    All_todo_retrive = All_todo.objects.all()
    fm = All_todo_form()



    return render(request,'ToDo_app/home.html', {'form':fm , 'done_data':retrive_done_data,'retrive_data':All_todo_retrive })

def todo_delete(request,id):
    if request.method=='POST':
     todo_data = All_todo.objects.get(pk=id)
     todo_data_history = History_todo.objects.get(pk=id)
     todo_data.delete()
     todo_data_history.delete()
     HttpResponseRedirect('ToDo_app/home.html')
    return render(request,'ToDo_app/delete.html')






    return render(request,'delete.html')

def todo_history(request):
    return render(request,'history.html')