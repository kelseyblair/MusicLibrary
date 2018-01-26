from django.urls import path, re_path

from . import views


app_name = 'musiclibrary'
urlpatterns = [
	path('', views.index, name="index"),
	path('search', views.search, name="search"),
	re_path(r'^search/(?P<pk>\w{0,200})$', views.searchresults, name="searchresults"),
	path('addsong', views.addsong, name="addsong"),
	path('list', views.list, name="list"),
]

