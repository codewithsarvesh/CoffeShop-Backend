from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from customers.models import User
from django.http import JsonResponse

from hashlib import sha256

@csrf_exempt
def register(request):
	username = request.POST.get('username')
	email = request.POST.get('email')
	password = request.POST.get('password')
	user_obj = User.objects.fliter(email=email)
	if len(user_obj)>=1:	
		return JsonResponse({'status':'409'})
	else:
		user = User(username=username,email=email,password=sha256(password.encode('utf-8')).hexdigest())
		user.save()
		return JsonResponse({'status':'200'})

@csrf_exempt
def login(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	user_obj = User.objects.fliter(email=email,password= sha256(password.encode('utf-8')).hexdigest())
	if len(user_obj)==1:
		return JsonResponse({'status':'200'})
	elif len(user_obj)==0:
		return JsonResponse({'status':'404'})
	else:
		return JsonResponse({'status':'500'})

