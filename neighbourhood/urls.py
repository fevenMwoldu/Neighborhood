"""neighbourhood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views 
from neighbours import views as my_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('neighbours.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^profile/$', my_views.add_profile, name='add-profile'),
    url(r'^post/$', my_views.add_post, name='add-post'),
    url(r'^bussiness/$', my_views.add_bussiness, name='add-bussiness'),
    url(r'^changeNeighbourhood/$', my_views.change_neighbourhood,name='change-neighbourhood')
]
