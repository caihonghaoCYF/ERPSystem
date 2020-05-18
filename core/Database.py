import sqlite3
from core.DatabaseConf import DatabaseConf

"""
l  NULL，值是NULL
l  INTEGER，值是有符号整形，根据值的大小以1,2,3,4,6或8字节存放
l  REAL，值是浮点型值，以8字节IEEE浮点数存放
l  TEXT，值是文本字符串，使用数据库编码（UTF-8，UTF-16BE或者UTF-16LE）存放
l  BLOB，只是一个数据块，完全按照输入存放（即没有准换）
"""

class Database(object):
    def __init__(self, url):
        super(Database, self).__init__()
        self.url = url
        self.con = None
        self.connect()

    def connect(self):
        self.con = sqlite3.connect(self.url)

    def createProductTable(self):
        tableName = DatabaseConf.productTableName
        productSql = "CREATE TABLE IF NOT EXISTS {tableName}({productId} TEXT PRIMARY KEY, \
                                                 {productName} TEXT,\
                                                 {attrId} TEXT, \
                                                 {unitId} TEXT , \
                                                 {canKapPrice} REAL, \
                                                 {lingShouPrice} REAL, \
                                                 {vipPrice} REAL, \
                                                 {piFaPrice} REAL, \
                                                 {defaultSupplier} TEXT , \
                                                 {categoryId} TEXT, \
                                                 {initStock} INTEGER, \
                                                 {minLimit} INTEGER, \
                                                 {maxLimit} INTEGER, \
                                                 {desc} TEXT)".format(tableName=tableName,
                                                                      productId="productId",
                                                                      productName="productName",
                                                                      attrId="attrId",
                                                                      unitId="unitId",
                                                                      canKapPrice="canKapPrice",
                                                                      lingShouPrice="lingShouPrice",
                                                                      vipPrice="vipPrice",
                                                                      piFaPrice="piFaPrice",
                                                                      defaultSupplier="defaultSupplier",
                                                                      categoryId="categoryId",
                                                                      initStock="initStock",
                                                                      minLimit="minLimit",
                                                                      maxLimit="maxLimit",
                                                                      desc="desc")
        print("创建product表")
        cursor = self.con.cursor()
        cursor.execute(productSql)
        cursor.close()


if __name__ == '__main__':
    database = Database(DatabaseConf.databaseName)
    database.createProductTable()
# con = sqlite3.connect("Test.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)")
# data = "5,'leon',22"
# cur.execute('INSERT INTO test VALUES (%s)' % data)
# cur.execute("INSERT INTO test values(?,?,?)", (6, "zgq", 20))
# cur.execute("select * from Test")
# for item in cur:
#     print(item)
