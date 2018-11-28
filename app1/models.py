# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lib.orm import ModelMixin

from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    SEX = (
        ('男','男'),
        ('女','女'),
    )
    nicname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)

    @property
    def age(self):
        now = datetime.data.today()
        birth_day = (self.birth_year,  self.birth_month, self.birth_day)
        return (now-birth_day)//365

    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            _profile, created = Profies.objects.get_or_create(id=self.id)
            self._profile = _profile
        return self._profile

    def _to_dict(self):
        return {
            'id': self.id,
            'nicname': self.nicname,
            'phonenum': self.phonenum,
            'sex': self.sex,
            'avatar': self.avatar,
            'location': self.location,
            'age': self.age,

        }


class Profies(models.Model,ModelMixin):
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )
    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')

    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=45, verbose_name='最大交友年龄')

    dating_sex = models.CharField(default='女', max_length=8, choices=SEX, verbose_name='匹配的性别')
    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')


