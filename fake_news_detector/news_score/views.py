from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import news_url
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
	template =loader.get_template('news_score/index.html')
	context ={

	}
	return render(request,'news_score/index.html',context)





#Here we try to get the input on the website
