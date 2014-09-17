from django.shortcuts import render
from django.http import HttpResponse

from config import CONFIG
count = CONFIG["count"]

# Create your views here.
def list(request):
	data = ""
	data = "Max is: " + str(count)
	for i in range(1,count+1):
		data += "<br/><a href='../chap/" + str(i) + "'>Chap " + str(i) + "</a>"
	return HttpResponse(data)

def chap(request, chapter):
	data = "<img width='100%' src='http://makervn.com/kimchi/data/chap_" + str(chapter) + ".jpg'/>"
	return HttpResponse(data)