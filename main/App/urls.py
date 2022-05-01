from django.urls import path
from . import views

urlpatterns = [
    path('',views.getAbstract, name="abs"),
]