from .import views
from django.urls import path

app_name="app"

urlpatterns = [
 
    path('',views.index,name='index'),
    path('mark_all_complete',views.mark_all_complete,name='mark_all_complete'),
    path('insert_todo',views.insert_todo,name='insert_todo'),
    path('mark_done/<id>',views.mark_done,name='mark_done'),
    path('delete_todo/<id>',views.delete_todo,name='delete_todo'),
]
