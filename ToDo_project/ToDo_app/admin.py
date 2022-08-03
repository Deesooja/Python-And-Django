from django.contrib import admin
from ToDo_app.models import All_todo,Done_todo, History_todo

# Register your models here.
@admin.register(All_todo,Done_todo,History_todo)
class All_todo_admin(admin.ModelAdmin):
    list_display=('id','todo','status')

class Done_todo_admin(admin.ModelAdmin):
    list_display=('id','todo','status')

class History_todo_admin(admin.ModelAdmin):
    list_display=('id','todo','status')