# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app1.logic import send_verify_code,check_vcode
from lib.http import render_json
from .models import *
from common.error import *

from django.shortcuts import render

# Create your views here.

def get_verify_code(request):
    '''

    :param request:
    :return:
    '''
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    data = {
        'code': 0,
        'data': None,
    }
    return render_json(None, 0)




def login(request):
    '''

    :param request:
    :return:
    '''
    phonenum = request.POST.get('phonenum')
    vcode =request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
        user, created = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        return render_json(user.to_dict(), 0)
    else:
        return render_json(None, VCODE_ERROR)



def get_profile(request):
    pass

def modify_profile(request):
    pass