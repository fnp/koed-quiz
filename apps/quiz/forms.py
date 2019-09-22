# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django import forms
from django.forms.widgets import RadioSelect
from django.utils.translation import ugettext_lazy as _
from quiz.models import Answer

class QuestionForm(forms.Form):
    answer = forms.ModelChoiceField(widget=RadioSelect,
        queryset=Answer.objects.all(), empty_label=None,
        error_messages={'required': _('Please select an option')})

    def __init__(self, instance, *args, **kwargs):
        r = super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['answer'].queryset = instance.answer_set.all()
        return r
