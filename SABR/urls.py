from django.conf.urls import patterns, url
from SABR import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^player/(?P<playerid>[\w\-]+)/$', views.player, name='player'),
      #  url(r'^search-form/$', views.search_form),
        url(r'^search/$', views.search),
        url(r'^api/get_players/', views.get_players, name='get_players'),
        url(r'^about', views.about, name='about'),
       
       
        
        
        
        

        
        )
        
        