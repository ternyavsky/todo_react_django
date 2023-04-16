from django.urls import path
from .views import task_list,task_detail
urlpatterns = [
    path('task',task_list,name='tasklist'),
    path('task/<str:pk>',task_detail,name='taskdetail')
]