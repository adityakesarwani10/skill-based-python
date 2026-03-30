from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('test/',views.test,name="test"),
    path('show/',views.show,name="show"),
    path('abcd/',views.abcd,name="abcd"),
    path('show_name/',views.show_name,name="show_name"),
    path('index/',views.index,name="index"),
    path('testing/',views.testing,name="testing"),
    path('testing2/',views.testing2,name="testing2"),
    path('submit/',views.submit,name="submit"),
    path('number/',views.number,name="number"),
]