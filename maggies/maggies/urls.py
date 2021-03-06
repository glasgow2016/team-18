"""maggies URL Configuration

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
from maggies import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^login', views.login_page),
    url(r'^logout', views.logout_page),
    url(r'^numSeen', views.numSeen),
    url(r'^recent', views.recent),
    url(r'^ajax_report_visitor_count', views.ajax_report_visitor_count),
    url(r'^ajax_check_for_daily_ids', views.ajax_check_for_daily_ids),
    url(r'^ajax_get_autofill_details', views.ajax_get_autofill_details),
    url(r'^', views.home),
]
