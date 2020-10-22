from django.conf.urls import url
from django.contrib import admin
from eventex.core.views import home

urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
]
