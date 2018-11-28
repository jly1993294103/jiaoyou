# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  django.shortcuts import render
from django.core.cache import cache
from app1.logic import send_verify_code

from django.shortcuts import render

# Create your views here.

def get_verify_code(request):
    '''

    :param request:
    :return:
    '''
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)




def login(request):
    '''

    :param request:
    :return:
    '''

def get_profile(request):
    pass

def modify_profile(request):
    pass