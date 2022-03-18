import MySQLdb



def getNasdaqGraphData():
    connect = MySQLdb.connect(user='root', password='1234',
                              database='dbpedia2016', charset="GBK")
    cursor = connect.cursor()

    sql = "select * from nasdaq_company_graph"
    cursor.execute(sql)
    nasdaqGraphData = [i[0].replace("dbr:", "") for i in cursor.fetchall()]
    return nasdaqGraphData


def getIndex(spliceNum, indexDict, indexList, tableName):
    nasdaqGraphData = getNasdaqGraphData()
    for data in nasdaqGraphData:
        data = data.replace("_", " ")
        if len(data) < spliceNum:
            continue
        splice = data[0:spliceNum]
        if splice not in indexDict:
            indexDict[splice] = data
        else:
            entityListStr = indexDict[splice]
            entityListStr += "||" + data
            indexDict[splice] = entityListStr
    for key, value in indexDict.items():
        indexList.append((key, value))
    connect = MySQLdb.connect(user='root', password='1234',
                              database='dbpedia2016', charset="GBK")
    cursor = connect.cursor()
    sql = "insert into {} values (%s, %s)".format(tableName)
    cursor.executemany(sql, indexList)
    connect.commit()
    connect.close()

if __name__ == '__main__':
    index_3 = {}
    index_3_List = []
    index_5 = {}
    index_5_List = []
    index_7 = {}
    index_7_List = []
    getIndex(3, index_3, index_3_List, "nasdaq_index_3")
    getIndex(5, index_5, index_5_List, "nasdaq_index_5")
    getIndex(7, index_7, index_7_List, "nasdaq_index_7")