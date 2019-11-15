# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class registration(models.Model):
    uname=models.TextField(max_length=20)
    pswd1=models.TextField(max_length=20)
    pswd2 = models.TextField(max_length=20)


class questions(models.Model):
    qno:models.IntegerField()
    name=models.TextField(max_length=100)
    options = models.TextField(max_length=200)
    correct_option = models.TextField(max_length=200)
    quiz = models.TextField(max_length=200)
    points = models.IntegerField()


class quiz(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
