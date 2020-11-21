import pymongo

print("数据库开始连接！")
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "news" in dblist:
  print("数据库已存在！")