from django.conf.urls import include, url
from django.contrib import admin
import eventex.core.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', eventex.core.views.home),
    url(r'^admin/', include(admin.site.urls)),
]