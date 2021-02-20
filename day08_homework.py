import pymysql
host="localhost"
user="root"
password=""
database="bank"
def update(sql,param):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def find(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()

# 文本文件导入数据库
# a = open("用户数据.txt", "r+", encoding="GBK")
# lis = a.readlines()
# a.close()
# for u in lis:
#     user_lis = u.replace("\n", "").split(",")
#     # print(user_lis)
#     sql="insert into abc values(%s,%s,%s)"
#     param=user_lis
#     update(sql,param)

# 总资产：
# sql="select sum(money) from abc"
# param=[]
# data=find(sql,param,mode="all",size=1)
# print("总资产为：",data[0][0])

# 数据库文件转为文本文件
sql="select * from abc"
param=[]
b = open("用户数据.txt", "a+", encoding="GBK")
m=find(sql,param,mode="all",size=1)
for i in m:
    a=i[0]+','+str(i[1])+','+str(i[2])+"\n"
    b.write(a)
b.closed

# 数据库文件转为文本文件
# sql="select * from abc"
# param=[]
# m=find(sql,param,mode="all",size=1)
# b = open("用户数据.txt", "a+", encoding="GBK")
# for i in range(0,6):
#     a="".join(str(m[i])).replace("(","").replace("'","").replace(")","").replace(" ","")
#     b.write(a+"\n")
# b.closed






