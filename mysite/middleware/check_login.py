from django.shortcuts import render, redirect
from mysite.views import log_in

def CheckLogin(get_response):
	def middleware(request):
		if '/admin/' in request.path or '/login/' in request.path or 'email' in request.session:
			response = get_response(request)
		else:
			response = redirect('/login/',request)
		
		return response
	return middleware
