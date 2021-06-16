import json
from django.core import serializers
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from common.models import User
from common.models import Poem
from common.langconv import *
from django.db.models import Q
from django.core.paginator import Paginator

def loginUser(request):
    na=request.POST.get("username")
    pwd=request.POST.get("password")
    
    try:
        qs = User.objects.get(name=na)
    except User.DoesNotExist:
        return HttpResponse('0')

    if qs.passwd==pwd:
        request.session['name'] = na
        request.session['password'] = pwd
        request.session.set_expiry(1200)
        if na!='mgr':
            request.session['usertype'] = 'user'
            return HttpResponse('1')
        else:
            request.session['usertype'] = 'mgr'
            return HttpResponse('2')
    
    return HttpResponse('0')
        
    
def registerUser(request):
    na=request.POST.get("username")
    pwd=request.POST.get("password")
    
    try:
        qs = User.objects.get(name=na)
    except User.DoesNotExist:
        User.objects.create(name=na ,passwd=pwd)
        return HttpResponse('1')
    
    return HttpResponse('0')


def logoutUser(request):
    na=request.session['name']

    request.session.flush()
    return HttpResponseRedirect('../login/index.html')


def getUser(request):
    try:
        na=request.session['name']
    except:
        return HttpResponse('-1')
    return HttpResponse(na)


def searchPoem(request):
    info=request.GET.get('info')
    page=request.GET.get('curr')
    size=request.GET.get('nums')

    info=Converter('zh-hant').convert(str(info))
    info=str(info).split(' ')

    retlist=[]

    for key in info:
        retlist+=list(Poem.objects.filter(content__contains=key).values())

    #创建分页对象
    ptr=Paginator(retlist,size)
    tmp=ptr.page(page)

    return JsonResponse({'code':0,'msg':'','count':len(retlist),'data':list(tmp)})
    