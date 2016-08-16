#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from my_blog.models import Article
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  #添加包
# Create your views here.
#root
def home(request):
    post_list = Article.objects.all() 
    paginator = Paginator(post_list, 2) #每页显示两个 
    page = request.GET.get('page')
    try:
    	post_list=paginator.page(page)
    except PageNotAnInteger:
    	post_list=paginator.page(1)
    except EmptyPage:
		post_list=paginator.paginator(paginator.num_pages)
		#p.num_pages page_number
		#p.page_range  page_num_list [1,2,3]
		#p1=p.page(1) go id page
		#p1.object_list first page data
		#p1.has_next   has_previous
		  
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request,id):
	try:
		post=Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	return render(request,'detail.html',{'post':post})

def archives(request):
	try:
		post_list=Article.objects.all()
	except Article.DoesNotExist:
		raise Http404
	return render (request,'archives.html',{'post_list':post_list})

def about_me(request):
	return render(request,'about_me.html')

def search_tag(request,tag):
	try:
		post_list=Article.objects.filter(category__iexact = tag)#ignore upper lower 
	except Article.DoesNotExist:
		raise Http404
	return render(request,'tag.html',{'post_list' : post_list})
