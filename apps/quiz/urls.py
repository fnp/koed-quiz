# -*- coding: utf-8 -*-
# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.conf.urls.defaults import *


urlpatterns = patterns('quiz.views',
    url(r'^$', 'question', name='quiz'),
    url(r'^q/(?P<slug>[^/]*)/$', 'question', name='quiz'),
    url(r'^r/(?P<slug>[^/]*)/$', 'result', name='quiz_result'),
)
