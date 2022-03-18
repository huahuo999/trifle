import MySQLdb
from queue import Queue


class Explore(object):
    def __init__(self, depth):
        self.depth = depth
        self.connect = MySQLdb.connect(user='root', password='1234',
                                      database='dbpedia2016', charset="GBK")
        self.cursor = self.connect.cursor()
        self.graphEntityList = []
        self.graphGraphList = []
        self.searchList = []
        self.notList = []

    def getNasdaqData(self):
        sql = "select * from nasdaq_company"
        self.cursor.execute(sql)
        nasdaqData = [i[0] for i in self.cursor.fetchall()]
        print(nasdaqData)
        return nasdaqData

    def StoO(self, target):
        entityOutList = []
        if "'" in target or '"' in target:
            target = target.replace("'", "''").replace('"', '""')
        sql = "select s,p,o from triples_dbp_new where s='{}'".format(target)
        self.cursor.execute(sql)
        for _ in self.cursor.fetchall():
            if "City108524735" not in self.getClassByEntity(
                    _[2]) and "Location100027167" not in self.getClassByEntity(_[2]):
                entityOutList.append(_[2])
                if len(_) != 0:
                    self.graphGraphList.append((0, _[0], _[2], _[1], _[1]))
        return entityOutList

    def OtoS(self, target):
        entityInList = []
        if "'" in target or '"' in target:
            target = target.replace("'", "''").replace('"', '""')
        sql = "select s,p,o from triples_dbp_new where o='{}'".format(target)
        self.cursor.execute(sql)
        for _ in self.cursor.fetchall():
            if "City108524735" not in self.getClassByEntity(
                    _[0]) and "Location100027167" not in self.getClassByEntity(_[0]):
                entityInList.append(_[0])
                if len(_) != 0:
                    self.graphGraphList.append((0, _[0], _[2], _[1], _[1]))
        return entityInList

    def mergeEntityList(self, target):
        entityInList, entityOutList = self.OtoS(target), self.StoO(target)
        entityList = entityOutList.copy()
        for _ in entityInList:
            if _ not in entityList:
                entityList.append(_)
        return entityList

    def getClassByEntity(self, target):
        if "'" in target or '"' in target:
            target = target.replace("'", "''").replace('"', '""')
        sql = "select type from type_transitive_yago_new where entity ='{}' group by type".format(target)
        self.cursor.execute(sql)
        this_answer = self.cursor.fetchall()
        class_List = []
        for class_ in this_answer:
            if "Wikicat" not in class_[0]:
                class_List.append(class_[0])
        return class_List

    def explore(self):
        nasdaqData = self.getNasdaqData()
        for data in nasdaqData:
            print(data)
            now = 0
            self.searchList.append(data)
            self.graphEntityList.append((0, data, data, 100-now*20, now))
            queue = Queue()
            queue.put(data)
            while not queue.empty():
                now += 1
                print("当前深度为", now)
                queue = self.bfs(queue, now)
                print("当前队列中有{}个".format(queue.qsize()))
                if now == self.depth:
                    break
        new_Connect = MySQLdb.connect(user='root', password='1234',
                                      database='nasdaq', charset="GBK")
        new_Cursor = new_Connect.cursor()
        sql1 = "insert into node values (%s, %s, %s, %s, %s)"
        sql = "insert into graph values (%s, %s, %s, %s, %s)"
        new_Cursor.executemany(sql, self.graphGraphList)
        new_Cursor.executemany(sql1, self.graphEntityList)
        new_Connect.commit()
        new_Connect.close()

    def bfs(self, queue, now):
        nextQueue = Queue()
        while not queue.empty():
            current = queue.get()
            if now == self.depth:
                for i in self.mergeEntityList(current):
                    if i not in self.searchList:
                        self.searchList.append(i)
                        self.graphEntityList.append((0, i, i, 100 - now * 20, now))
                continue
            for i in self.mergeEntityList(current):
                if i not in self.searchList:
                    self.graphEntityList.append((0, i, i, 100-now*20, now))
                    self.searchList.append(i)
                    nextQueue.put(i)
        return nextQueue


if __name__ == '__main__':
    explore = Explore(2)
    explore.explore()
