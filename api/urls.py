from django.urls import path
from api import views
from django.views.generic import TemplateView

urlpatterns=[
    path('resources',views.Resources.as_view()),  #mapping the resource view  (
    path('',TemplateView.as_view(template_name="index.html"))    #mapping the templateview


]