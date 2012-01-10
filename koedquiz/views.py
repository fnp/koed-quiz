# -*- coding: utf-8 -*-
# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.shortcuts import render

from django.conf import settings
from quiz.models import Quiz


def home(request):
    quiz = Quiz.current()
    return render(request, "home.html", locals())
