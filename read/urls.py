from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^chap/(\w*)', views.chap, name="chap"),
    url(r'^list', views.list, name="list"),
)
