from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
	if request.method == 'POST':
		return HttpResponse("login")
	return render(request, 'login.html')

def signup(request):
	#If they click the link to signup they should come here. 
	#When they click register they should be transferred elsewhere 
	#using a redirect
	if request.method == 'POST':
		return HttpResponse("signup")
	return render(request, 'signup.html')