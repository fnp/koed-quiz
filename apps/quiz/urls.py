from django.conf.urls.defaults import *


urlpatterns = patterns('quiz.views',
    url(r'^$', 'question', name='quiz'),
    url(r'^q/(?P<slug>[-a-z0-9]*)/$', 'question', name='quiz'),
    url(r'^r/(?P<slug>[-a-z0-9]*)/$', 'result', name='quiz_result'),
)
