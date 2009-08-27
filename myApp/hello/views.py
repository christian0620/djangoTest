# Create your views here.
from django.shortcuts import render_to_response
import datetime

def time(request,offset):
	now = datetime.datetime.now()
	time = now + datetime.timedelta(hours = int(offset))
	return render_to_response('hello.html',{"time":time})
