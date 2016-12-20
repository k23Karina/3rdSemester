"""IShop URL Configuration

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
from website import views as site_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', site_views.auth_login, name='auth_login'),
    url(r'^logout/$', site_views.auth_logout, name='auth_logout'),
    url(r'^category/$', site_views.category, name='category'),
    url(r'^$', site_views.home, name='home'),
    url(r'^(?P<category_name>[a-zA-Z]+)/$', site_views.tovar_list, name='tovar_list'),
url(r'^(?P<category_name>[a-zA-Z]+)/(?P<towar_id>[0-9]+)$', site_views.towar_info, name='tovar_info'),
]
