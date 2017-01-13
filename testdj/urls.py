"""testdj URL Configuration

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
#
# from django.conf.urls import url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
from django.conf.urls import *

from testdj.testdb import delete_db
from testdj.testdb import get_db
from testdj.testdb import testdb
from testdj.testdb import update_db
from testdj.view import base
from testdj.view import hello
from testdj.view import hello2
from testdj.view import helloextends
from testdj.view import init

urlpatterns = [url('^delete_db/$', delete_db), url('^update_db/$', update_db), url('^get_db/$', get_db),
               url('^testdb/$', testdb), url('^base/$', base), url('^helloextends/$', helloextends),
               url('^hello2/$', hello2),
               url('^hello/$', hello), url('', init)]
