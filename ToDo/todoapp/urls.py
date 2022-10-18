#app urls
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('additem',views.todoAPIview.as_view(),name="additem")
]
