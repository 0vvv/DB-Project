import json
from django.http import HttpResponse
from common.models import User
from common.models import Poem
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from common.zh_wiki import *
from common.langconv import *

def showUser(request):
#返回所有用户的用户名和ID
    page=request.GET.get('curr')
    size=request.GET.get('nums')

    retlist=list(User.objects.values("id", "name"))

    #创建分页对象
    ptr=Paginator(retlist,size)
    tmp=ptr.page(page)

    return JsonResponse({'code':0,'msg':'','count':len(retlist),'data':list(tmp)})

def delUser(request):
    uid=request.POST.get("id")
    try:
        tmp = User.objects.get(id=uid)
    except:
        return HttpResponse('-1')

    tmp.delete()
    return HttpResponse('0')

def showPoem(request):
    #返回所有诗
    page=request.GET.get('curr')
    size=request.GET.get('nums')

    retlist=list(Poem.objects.values("id", "title", "author", "content"))

    #创建分页对象
    ptr=Paginator(retlist,size)
    tmp=ptr.page(page)

    return JsonResponse({'code':0,'msg':'','count':len(retlist),'data':list(tmp)})

def delPoem(request):
    pid=request.POST.get("id")
    try:
        tmp=Poem.objects.get(id=pid)
    except:
        return HttpResponse('-1')

    tmp.delete()
    return HttpResponse('0')

def editpoem(request):
    id = request.POST.get("id")
    content = request.POST.get("content")
    #title = request.POST.get("title")
    #author = request.POST.get("author")

    try:
        tmp = Poem.objects.get(id=id)
    except:
        return HttpResponse('-1')

    tmp.content=content
    tmp.save()
    return HttpResponse('0')

'''
    if(tmp.title != title):
        tmp.title=title
    if(tmp.author !=author):
        tmp.author=author
'''

def searchpoem(request):
    info=request.GET.get('info')
    page=request.GET.get('curr')
    size=request.GET.get('nums')

    info=Converter('zh-hant').convert(str(info))
    info=str(info).split(' ')
    retlist=[]

    for key in info:
        retlist+=list(Poem.objects.filter(content__contains=key).values())
    #创建分页对象
    ptr=Paginator(retlist, size)
    tmp=ptr.page(page)
    return JsonResponse({'code':0,'msg':'','count':len(retlist),'data':list(tmp)})


def searchuser(request):
    info=request.GET.get('info')
    page=request.GET.get('curr')
    size=request.GET.get('nums')

    info=Converter('zh-hant').convert(str(info))
    info=str(info).split(' ')
    retlist=[]

    for key in info:
        retlist+=list(User.objects.filter(name__contains=key).values())
    #创建分页对象
    ptr=Paginator(retlist, size)
    tmp=ptr.page(page)
    return JsonResponse({'code':0,'msg':'','count':len(retlist),'data':list(tmp)})

'''
def addPoem(request):
    title = request.POST.get("title")
    author = request.POST.get("author")
    content = request.POST.get("content")

    res = Poem.objects.filter(title=title, author=author, content=content).values()

    if res.exists():
        return HttpResponse('-1')

    Poem.objects.create(title=title, author=author, content=content)
    return HttpResponse('0')
'''