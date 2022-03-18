import json

from django.db.models import Q

from nasdaq.models import Nodes, Links
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def getEchartsData(request):
    # 接收传递过来的查询条件 -- axios默认json
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    # 使用ORM获取所有满足条件的学生信息
    try:
        obj_nodes = Nodes.objects.filter(Q(entity__icontains=data['inputstr'])).values('entity', 'des', 'symbolsize', 'depth')
        print(obj_nodes)
        obj_links = Links.objects.filter(Q(s__icontains=data['inputstr'])|Q(o__icontains=data['inputstr'])).values('s', 'p', 'o').distinct()
        nodes = list(obj_nodes)
        links = list(obj_links)
        print(links)
        return JsonResponse({'code': 1, 'nodes': nodes, 'links': links})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "查询学生信息出现异常，具体错误：" + str(e)})
        # 如果出现异常返回

