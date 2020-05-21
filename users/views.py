from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Users
# Create your views here.

def index(request):
	users =  Users.objects.all()
	data = { 'users': users }
	return render(request, 'users/list.html', data)

def add(request):
	data = request.POST
	
	if data['user_name'] == '':
		return HttpResponseRedirect(reverse('users:index', args=['error_message' ,'empty datas'] ))
		#return render(request, 'users/list.html',{'error_message' : 'empty data'})
	else:
		Users.objects.create(user_name = data['user_name'])
		data = {'users' : Users.objects.all()}
		return render(request, 'users/list.html', data)
	
def remove(request, id ):
	user = Users.objects.get(id=id)
	user.delete()

	users =  Users.objects.all()
	data = { 'users': users }
	return render(request, 'users/list.html', data)
