"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from my_blog.views import home,detail,archives,about_me,search_tag
urlpatterns = [
    #/yoursiye/home/detail/
    #url(r'detail/(?P<id>]\d+)/$',detail,name="detail")
    #href={% url 'detail' args %}
    #href={% url 'detail' id %}   /detail/1 args by views.py 
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^detail/(?P<id>\d+)/$',detail,name='detail'),
    url(r'^archives/$',archives,name="archives"),
    url(r'^aboutme/$',about_me,name="about_me"),
    url(r'^tag(?P<tag>\w+)$',search_tag,name="search_tag"),

]
