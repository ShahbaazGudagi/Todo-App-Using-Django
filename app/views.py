from turtle import update
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Todoitem

# Create your views here.
#main todo HTml file or Home page 
def index(request):
    done_items=Todoitem.objects.filter(todo_status="DONE")
    not_done_items=Todoitem.objects.filter(todo_status="NOT DONE")
    context={
        "done_items":done_items,
        "not_done_items":not_done_items,
    }
    return render(request,'app/index.html',context)

#selecting all the todo list once at a time
def mark_all_complete(request):
    Todoitem.objects.filter(todo_status="NOT DONE").update(todo_status="DONE")

    return HttpResponseRedirect(reverse("app:index"))

#inserting the todo
def insert_todo(request):
    todo_text=request.POST['todo_text']
    obj=Todoitem(todo_text=todo_text)
    obj.save()
    return HttpResponseRedirect(reverse('app:index'))




#marking the todo & sending it to Already done list
def mark_done(request,id):
    obj=Todoitem.objects.get(id=id)
    obj.todo_status="DONE"
    obj.save()
    return HttpResponseRedirect(reverse("app:index"))


#Deleting the Todo items from Already done todo list
def delete_todo(request,id):
    obj=Todoitem.objects.get(id=id)
    obj.delete()
    
    return HttpResponseRedirect(reverse("app:index"))