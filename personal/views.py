from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from blog.views import get_blog_queryset
from blog.models import BlogPost

BLOG_POSTS_PER_PAGE = 10

def home_screen_view(request):
    	
	context = {}

	# Search
	#query = ""
	#if request.GET:
	#	query = request.GET.get('q', '')
	#	context['query'] = str(query)

	blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
	

	context['blog_posts'] = blog_posts

	return render(request, "base.html", context)

