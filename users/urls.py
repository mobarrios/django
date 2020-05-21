from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
	path('',views.index, name='index'),
	path('add/', views.add, name='add'),
	path('<int:id>/del/', views.remove , name='remove'),

]