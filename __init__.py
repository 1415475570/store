import pymongo
import requests
import pymysql

# 请求url地址获取响应

response = requests.post(url="http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent",
                         data={"username":"jason"})

# 取出响应的所有学生数据
response.encoding = "utf-8"

# 把响应的数据传唤成字典
users = response.json()  #
# print(users)

# 连接数据库
client=pymongo.MongoClient("mongodb://localhost:27017")
# 展示数据库
lists=client.list_database_names()
# print(lists)
# 选择数据库，然后插入数据
db = client["aa"]
user =users

# 插入多条数据
# status=db["student"].insert_many(user)

# 修改
# db["student"].update_many({"username":"王朔"},{"$set":{"username":"张三"}})

# 多条件查询
# for i in db["student"].find({"$or":[{"username":"贾生"},{"username":"张三"}]}):
#     print(i)

# 删除数据
# db["student"].delete_one({"username":"MU"})

db["student"].groupby({ "courName": "$courName"})

