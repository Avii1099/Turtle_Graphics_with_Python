from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [

	{
		'author': 'Arvind',
		'title': 'Blog Post 1',
		'content': '1st post content',
		'date_posted': 'July 18, 2021'
	},

	{
		'author': 'Avii',
		'title': 'Blog Post 2',
		'content': '2nd post content',
		'date_posted': 'Aug 18, 2021'	
	}

]

def home(request):
	context = {
	'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})



