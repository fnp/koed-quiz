# -*- coding: utf-8 -*-
# This file is part of KOED-Quiz, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.db import models
from django.contrib.sites.models import Site
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.conf import settings


class Quiz(Site):
    description = models.TextField()
    footer = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _('quiz')
        verbose_name_plural = _('quizzes')

    @classmethod
    def current(cls):
        return cls.objects.get(id=settings.SITE_ID)

    def start(self):
        return self.question_set.all()[0]

    @models.permalink
    def get_absolute_url(self):
        return ('quiz', )

    def where_to(self):
        try:
            return Result.objects.get(quiz=self).get_absolute_url()
        except Result.DoesNotExist:
            # just go to the beginning
            return self.get_absolute_url()


@python_2_unicode_compatible
class Result(models.Model):
    quiz = models.ForeignKey(Quiz)
    slug = models.SlugField(db_index=True)
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = _('result')
        verbose_name_plural = _('results')
        ordering = ['quiz', 'title']

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('quiz_result', [self.slug])


@python_2_unicode_compatible
class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    slug = models.SlugField(db_index=True)
    ordering = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ['quiz', 'ordering']
        unique_together = [['quiz', 'slug'], ['quiz', 'ordering']]

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('quiz', [self.slug])

    def where_to(self):
        later = self.quiz.question_set.filter(ordering__gt=self.ordering)
        if later.exists():
            return later[0].get_absolute_url()
        else:
            return self.quiz.where_to()


@python_2_unicode_compatible
class Answer(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(Question)
    go_to = models.ForeignKey(Question, null=True, blank=True,
            related_name='go_tos')
    result = models.ForeignKey(Result, null=True, blank=True)
    ordering = models.SmallIntegerField()

    class Meta:
        verbose_name = _('answer')
        verbose_name_plural = _('answers')
        ordering = ['question', 'ordering']

    def __str__(self):
        return self.title

    def where_to(self):
        # follow explicit redirects
        if self.result:
            return self.result.get_absolute_url()
        elif self.go_to:
            return self.go_to.get_absolute_url()

        # or just get the next question
        return self.question.where_to()
