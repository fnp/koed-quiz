# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.urls import path
from . import views


urlpatterns = [
    path('', views.question, name='quiz'),
    path('q/<slug>/', views.question, name='quiz'),
    path('r/<slug>/', views.result, name='quiz_result'),
]
