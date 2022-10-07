from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import re
from . import service
# Create your views here.
def index(request):
    # 1 获得数据 通过service模块
    poems = service.getAllPoems()
    # 2 render渲染首页
    return render(request, 'poem/index.html', {'poems':poems})

def detail(request, id):
    poem = service.getPoem(id)
    # poem.contents = poem.content.split(' ')
    # 但是，如果内容使用,.等分割呢 引入re吧 
    poem.contents = re.split(r'[\s,.，。]', poem.content)
    return render(request, 'poem/detail.html', {'poem':poem})

def add(request):
    return render(request, 'poem/add.html', {})

def svc_add(request):
    # 1 获得form提交的数据 通过POST
    title = request.POST['title'] # 'title'要和input的name保持一致，变量名title可以随意
    content = request.POST['content'] 
    # 2 将数据提交到数据库 
    service.addPoem(title, content)
    # 3 重定向到首页 
    return HttpResponseRedirect( reverse('poem:index') )
    # 模板中的{% url %}标签的功能 与 reverse的功能是一致的 

def delete(request, id):
    # 根据id在数据库中删除诗歌
    service.deletePoem(id)
    # 重定向到首页
    return HttpResponseRedirect( reverse('poem:index') )

def edit(request, id):
    # 获得要修改的诗歌
    poem = service.getPoem(id)
    # 渲染修改页面
    return render(request, 'poem/edit.html', {'poem':poem})

def svc_edit(request, id):
    # 获得修改后的title和content
    title = request.POST['title'] # 'title'要和input的name保持一致，变量名title可以随意
    content = request.POST['content'] 
    # 提交id title content数据到service去修改
    service.editPoem(id, title, content)
    # 重定向到首页 
    return HttpResponseRedirect( reverse('poem:index') )
