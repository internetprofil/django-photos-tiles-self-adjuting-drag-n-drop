from django.conf.urls.defaults import *

urlpatterns = patterns('weddings.views',
    url(r'^$', 'story_list', name='story_list'),
    url(r'^(?P<slug>[-\w]+)$', 'story_detail', name='story_detail'),
)

