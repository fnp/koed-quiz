from django.conf.urls.defaults import *


urlpatterns = patterns('quiz.views',
    url(r'^$', 'question', name='quiz'),
    url(r'^q/(?P<slug>[^/]*)/$', 'question', name='quiz'),
    url(r'^r/(?P<slug>[^/]*)/$', 'result', name='quiz_result'),
)
