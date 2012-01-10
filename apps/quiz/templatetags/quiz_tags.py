# -*- coding: utf-8 -*-
# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django import template
from django.utils.safestring import mark_safe
from quiz.models import Quiz

register = template.Library()


@register.simple_tag
def quiz_footer():
    return mark_safe(Quiz.current().footer)
