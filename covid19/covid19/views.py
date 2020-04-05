from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from .models import News

# Create your views here.
def index(request):

	dests = Destination.objects.all()
	news = News.objects.all()
	
	

	return render(request,'index.html', {'dests': dests,'temp': '9548983560','news': news})
	

	
# Create your views here.
