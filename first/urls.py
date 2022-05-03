from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index , name = "Home"),
    path ("home", views.index , name = "Home"),
    path("view",views.viewData,name = "ViewData"),




    ]