import json

import MySQLdb
from django.db.models import Q
from queue import Queue
from nasdaq.models import Nodes, Links
from django.shortcuts import render
from django.http import JsonResponse


# class Explore(object):
#     def __init__(self, depth, target):
#         self.depth = depth
#         self.target = target
#         self.connect = MySQLdb.connect(user='root', password='1234',
#                                        database='dbpedia2016', charset="GBK")
#         self.cursor = self.connect.cursor()
#         self.nodes = []
#         self.links = []
#
#     def getClassByEntity(self, target):
#         if "'" in target or '"' in target:
#             target = target.replace("'", "''").replace('"', '""')
#         sql = "select type from type_transitive_yago_new where entity ='{}' group by type".format(target)
#         self.cursor.execute(sql)
#         this_answer = self.cursor.fetchall()
#         class_List = []
#         for class_ in this_answer:
#             if "Wikicat" not in class_[0]:
#                 class_List.append(class_[0])
#         return class_List
#
#     def explore(self):
#         now = 0
#         queue = Queue()
#         queue.put(self.target)
#         while not queue.empty():
#             queue = self.bfs(queue, now)
#             if now == self.depth:
#                 break
#             now += 1
#         return self.nodes, self.links
#
#     def bfs(self, queue, now):
#         nextQueue = Queue()
#         while not queue.empty():
#             current = queue.get()
#             if "'" in current or '"' in current:
#                 current = current.replace("'", "''").replace('"', '""')
#             if now == self.depth:
#                 continue
#
#             sql = "select s,p,o from triples_dbp_new where s='{}'".format(current)
#             print(sql)
#             self.cursor.execute(sql)
#             for _ in self.cursor.fetchall():
#                 if "City108524735" not in self.getClassByEntity(
#                         _[2]) and "Location100027167" not in self.getClassByEntity(_[2]):
#                     nodeDicSource = {'id': str(len(self.nodes)),
#                                      'name': _[0],
#                                      'des': _[0],
#                                      'symbolSize': 100 - now * 20,
#                                      'category': now - 1}
#                     self.nodes.append(nodeDicSource)
#                     nodeDicTarget = {'id': str(len(self.nodes)),
#                                      'name': _[2],
#                                      'des': _[2],
#                                      'symbolSize': 100 - now * 20,
#                                      'category': now}
#                     self.nodes.append(nodeDicTarget)
#                     link_Dic = {
#                         'source': nodeDicSource['id'],
#                         'target': nodeDicTarget['id'],
#                         'name': _[1],
#                         'des': _[1],
#                     }
#                     self.links.append(link_Dic)
#                     nextQueue.put(_[2])
#             sql1 = "select s,p,o from triples_dbp_new where o='{}'".format(current)
#             print(sql1)
#             self.cursor.execute(sql1)
#             for _ in self.cursor.fetchall():
#                 if "City108524735" not in self.getClassByEntity(
#                         _[0]) and "Location100027167" not in self.getClassByEntity(_[0]):
#                     nodeDicSource = {'id': str(len(self.nodes)),
#                                      'name': _[0],
#                                      'des': _[0],
#                                      'symbolSize': 100 - now * 20,
#                                      'category': now - 1}
#                     self.nodes.append(nodeDicSource)
#                     nodeDicTarget = {'id': str(len(self.nodes)),
#                                      'name': _[2],
#                                      'des': _[2],
#                                      'symbolSize': 100 - now * 20,
#                                      'category': now}
#                     self.nodes.append(nodeDicTarget)
#                     link_Dic = {
#                         'source': nodeDicSource['id'],
#                         'target': nodeDicTarget['id'],
#                         'name': _[1],
#                         'des': _[1],
#                     }
#                     self.links.append(link_Dic)
#                     nextQueue.put(_[0])
#         return nextQueue


# Create your views here.
def getEchartsData(request):
    # 接收传递过来的查询条件 -- axios默认json
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    # 使用ORM获取所有满足条件的学生信息
    try:
        obj_nodes = Nodes.objects.filter(Q(name=data['inputstr'])).values('id', 'name', 'des', 'symbolSize',
                                                                          'category')
        nodes = list(obj_nodes)
        obj_links = Links.objects.filter(
            Q(source=data['inputstr']) | Q(target=data['inputstr'])).values('source', 'name', 'des',
                                                                            'target').distinct()
        links = list(obj_links)
        for link in links:
            if link['target'] == data['inputstr']:
                search_node = Nodes.objects.filter(Q(name=link['source'])).values()
            else:
                search_node = Nodes.objects.filter(Q(name=link['target'])).values()
            search_nodes = list(search_node)
            for _ in search_nodes:
                nodeDic = {'id': _['id'],
                           'name': _['name'],
                           'des': _['des'],
                           'symbolSize': _['symbolSize'],
                           'category': _['category']}
                if nodeDic not in nodes:
                    nodes.append(nodeDic)
        node_IdDic = {}
        new_Links = []
        for node in nodes:
            node_IdDic[node['name']] = str(node['id'])
        print(node_IdDic)
        for link in links:
            link_Dic = {
                'source': node_IdDic[link['source']],
                'target': node_IdDic[link['target']],
                'name': link['name'],
                'des': link['des'],
            }
            new_Links.append(link_Dic)
        print(new_Links)
        return JsonResponse({'code': 1, 'nodes': nodes, 'links': new_Links})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "查询知识图谱出现异常，具体错误：" + str(e)})
        # 如果出现异常返回


def getEchartsData1(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        entity = data['inputstr']
        depth = data['depth']

        explore = Explore(depth, entity)
        nodes, links = explore.explore()
        return JsonResponse({'code': 1, 'nodes': nodes, 'links': links})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "查询知识图谱出现异常，具体错误：" + str(e)})
        # 如果出现异常返回
