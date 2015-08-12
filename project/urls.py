"""cereal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'main.views.home'),
    url(r'^cereal_list_view/$', 'main.views.cereal_list_view'),
    url(r'^cereal_search/(?P<cereal>\w+)/$', 'main.views.cereal_search'),
    url(r'get_cereal_search/$', 'main.views.get_cereal_search'),
    url(r'^manu_list_view/$', 'main.views.manu_list_view'),
    url(r'^manu_search/(?P<manufacturer>\w+)/$', 'main.views.manu_search'),
    url(r'^get_cereal_manufacturer/$', 'main.views.get_cereal_manufacturer'),
    #url(r'^get_cereal_nutri/$', 'main.views.get_cereal_nutri'),
    url(r'^get_cereal_search/$', 'main.views.get_cereal_search'),
    url(r'^cereal_list_template/$', 'main.views.cereal_list_template'),
    url(r'^cereal_list_template2/$', 'main.views.cereal_list_template2'),
    url(r'^cereal_detail/(?P<pk>\d+)/$', 'main.views.cereal_detail'),
    url(r'^form_view/$', 'main.views.form_view'),
    url(r'^form_view2/$', 'main.views.form_view2'),
    url(r'^cereal_create/$', 'main.views.cereal_create'),
    url(r'^signup/$', 'main.views.signup'),
    url(r'^login_view/$', 'main.views.login_view'),
    url(r'^logout_view/$', 'main.views.logout_view'),


]
