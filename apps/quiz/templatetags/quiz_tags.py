# -*- coding: utf-8 -*-
# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django import template
from django.utils.safestring import mark_safe
from quiz.models import Quiz

register = template.Library()


@register.simple_tag(takes_context=True)
def quiz_footer(context):
    return mark_safe(context.get('request').current_quiz.footer)
