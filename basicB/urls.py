from django.urls import path
from . import views
app_name="basicB"
urlpatterns = [
    path('templates/', views.basicB_template, name='basicB_template'),
    path('templates/basicB_form_show', views.basicB_form_show, name='basicB_form_show'),
    path('templates/basicB_form', views.basicB_form, name='basicB_form'),
    path('templates/basicB_form_show2', views.basicB_form_show2, name='basicB_form_show2'),
    path('templates/basicB_form2', views.basicB_form2, name='basicB_form2'),
    path('templates/basicB_form_show3', views.basicB_form_show3, name='basicB_form_show3'),
]
