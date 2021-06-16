import json
from django.core import serializers
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from common.models import Collection
from common.models import User
from common.models import Review
from django.db.models import Q
from django.core.paginator import Paginator

def addCollect(request):
    na=request.POST.get("name")
    pid=request.POST.get("poem_id")
    title=request.POST.get("title")
    content=request.POST.get("content")


    qs=User.objects.get(name=na)
    uid=qs.id

    res=Collection.objects.filter(user_id=uid,poem_id=pid).values()
    if res.exists():
        return HttpResponse('-1')
    
    Collection.objects.create(user_id=uid,poem_id=pid,title=title,content=content)
    return HttpResponse('0')

def checkCollect(request):
    na=request.session['name']
    page=request.GET.get('curr')
    size=request.GET.get('nums')

    qs=User.objects.get(name=na)
    uid=qs.id

    retlist=list(Collection.objects.filter(user_id=uid).values())

    #创建分页对象
    ptr=Paginator(retlist,size)
    tmp=ptr.page(page)

    return JsonResponse({'code':0,'msg':'','count':len(retlist),'data':list(tmp)})

def delCollect(request):
    id=request.POST.get("id")
    try:
        tmp=Collection.objects.get(id=id)
    except:
        return HttpResponse('-1')
    
    tmp.delete()
    return HttpResponse('0')
    

def addNote(request):
    na=request.POST.get("name")
    pid=request.POST.get("poem_id")
    note=request.POST.get("note")
    title=request.POST.get("title")
    content=request.POST.get("content")

    qs=User.objects.get(name=na)
    uid=qs.id

    try:
        res=Review.objects.get(user_id=uid,poem_id=pid)
    except:
        Review.objects.create(user_id=uid,poem_id=pid,poem_title=title,content=note,poem_content=content)
        return HttpResponse('0')
    
    return HttpResponse('-1')

def checkNote(request):
    na=request.session['name']
    page=request.GET.get('curr')
    size=request.GET.get('nums')

    qs=User.objects.get(name=na)
    uid=qs.id

    retlist=list(Review.objects.filter(user_id=uid).values())

    #创建分页对象
    ptr=Paginator(retlist,size)
    tmp=ptr.page(page)

    return JsonResponse({'code':0,'msg':'','count':len(retlist),'data':list(tmp)})


def delNote(request):
    id=request.POST.get("id")
    try:
        tmp=Review.objects.get(id=id)
    except:
        return HttpResponse('-1')
    
    tmp.delete()
    return HttpResponse('0')

def changeNote(request):
    id=request.POST.get("id")
    content=request.POST.get("content")
    try:
        tmp=Review.objects.get(id=id)
    except:
        return HttpResponse('-1')
    
    tmp.content=content
    tmp.save()

    return HttpResponse('0')