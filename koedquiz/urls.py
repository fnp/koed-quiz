# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('', TemplateView.as_view(template_name="quiz/home.html"), name='main_page'),

    path('quiz/', include('quiz.urls')),

    path('admin/', admin.site.urls),
]
