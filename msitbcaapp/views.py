from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def homepage(request):
	return render(request, "index.html")

def testpage(request):
	return render(render, "test.html")

def saveUser(request):
	if request.method=='POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		uname = request.POST['uname']
		email = request.POST['email']
		passwd = request.POST['password']
		ck_passwd = request.POST['ck_password']
		if passwd == ck_passwd:
			user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, email=email, password=passwd)
			print(user)
			user.save()
			return redirect('/')
		else:
			messages.error(request, 'Failed')
			return redirect('/')
	else:
		return HttpResponse('<script>alert("request error..!!")</script>')

def login(request):
	if request.method=='POST':
		username = request.POST['username']
		pwd = request.POST['password']
		user = auth.authenticate(username=username, password=pwd)
		if user is not None:
			auth.login(request, user)
			return redirect('/home')
		else:
			messages.error(request, 'Wrong credentials')
			return redirect('/')
	else:
		return HttpResponse('<script>alert("request error..!!")</script>')

def afterLogin(request):
	return render(request, "home.html")