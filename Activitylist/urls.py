from django.urls import path


from . import views

urlpatterns = [

    path('', views.Homepage.as_view(), name='home'),
    path('dates', views.DateCreateView.as_view(), name='createdates'),

]


