from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todolist.views import finish_task, show_todolist, register, login_user, logout_user, show_create_task, create_task, delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_task, name='show-create-task'),
    path('add-task/', create_task, name='create-task'),
    path('delete-task/<int:i>/', delete_task, name='delete-todo'), 
    path('finish-task/<int:i>/', finish_task, name='finish-task')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)