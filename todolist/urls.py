from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todolist.views import finish_task, show_todolist, register, login_user, logout_user, show_create_task, create_task, delete_task, show_todolist_json, add_json_task, delete_json_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_task, name='show-create-task'),
    path('add-task/', create_task, name='create-task'),
    path('delete-task/<int:i>/', delete_task, name='delete-todo'), 
    path('finish-task/<int:i>/', finish_task, name='finish-task'),
    path('json/', show_todolist_json, name="show_todolist_json"),
    path('add/', add_json_task, name="add_json_task"),
    path('delete/<int:id>/', delete_json_task, name='delete_json_task'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)