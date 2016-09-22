from django.conf.urls import include, url
from views import register, login, profile, logout, home

urlpatterns = [
    url(r'^$', home ,name='index'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
]