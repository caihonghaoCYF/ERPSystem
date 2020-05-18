from core.Database import Database
from model.ProductEntity import ProductEntity
from core.DatabaseConf import DatabaseConf
import re

#https://blog.csdn.net/GuoQiZhang/article/details/91344509
class BaseMapper(object):
    def __init__(self, obj, objName):
        super(BaseMapper, self).__init__()
        self.allMember = obj.__dict__
        self.pojo = obj
        self.objName = objName
        self.database = Database(DatabaseConf.databaseName)
        self.conn = self.database.con

    def baseFind(self, id=None):

        tempSqlStr = "SELECT "
        tempSqlList = []
        tempId = ""
        for key in self.allMember.keys():
            if key is "table":
                continue
            if not hasattr(self.pojo, key):
                continue
            if id is not None:
                if re.search('id', key, re.IGNORECASE):
                    tempId = key

            tempSqlStr += f'{key},'
            tempSqlList.append(key)

        tempSqlStr = tempSqlStr[:-1]
        tempSqlStr = tempSqlStr + " from " + self.pojo.table
        if id is not None:
            tempSqlStr += tempSqlStr + "where "+tempId+" = " + id
        # SELECT * FROM test"
        cursor = self.conn.cursor()
        cursor.execute(tempSqlStr)
        dataList = []
        for itemIndex, itemValue in enumerate(cursor):
            # 反射
            modelModule = __import__(DatabaseConf.modelName)
            mPy = getattr(modelModule, self.objName)
            objClassName = getattr(mPy, self.objName)
            newPojo = objClassName()

            for index, key in enumerate(tempSqlList):
                if hasattr(newPojo, key):
                    setattr(newPojo, key, itemValue[index])
            dataList.append(newPojo)

        cursor.close()
        return dataList

    def baseInsert(self, data):
        # "INSERT INTO test values(?,?,?)", (6, "zgq", 20)
        baseSql = "INSERT INTO " + self.pojo.table +" values ("
        tempKeyStr = ""
        tempValueList = []
        for key in self.allMember.keys():
            if key is "table":
                continue
            if not hasattr(data, key):
                continue
            tempKeyStr += '?,'
            tempValueList.append(f'{getattr(data, key)},')

        tempKeyStr = tempKeyStr[:-1]+")"
        # tempKeyStr = "%s)"
        tempValueTuple = tuple(tempValueList)
        baseSql = baseSql + tempKeyStr
        print(baseSql, tempValueTuple)

        cursor = self.conn.cursor()
        cursor.execute(baseSql, tempValueTuple)
        cursor.close()

    def insert(self, data):
        self.baseInsert(data)


    def update(self, data):
        #cur.execute("UPDATE test SET name=? WHERE id=?", ("nihao", 1))

        pass

    def findById(self, id):
        pass

    def findAll(self):
        pass

    def deleteById(self, id):
        pass


if __name__ == '__main__':
    p = ProductEntity()
    base = BaseMapper(p, "ProductEntity")
    p.table = "product"
    p.productId = "xxxx0001"
    p.attrId = 1
    p.desc = "sss"
    p.categoryId = 12
    p.minLimit = 1
    baseMapper = BaseMapper(p, "ProductEntity")
    baseMapper.insert(p)
    p2 = ProductEntity()
    p2.productId = "xxxx0002"
    p2.table = "product"
    p2.attrId = 3
    p2.desc = "sss"
    p2.categoryId = 12
    p2.minLimit = 1
    baseMapper.insert(p2)
    data = baseMapper.baseFind("xxxx0002")
    for da in data:
        print(da.productId)