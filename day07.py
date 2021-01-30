import pymysql

# 添加
# con=pymysql.connect(host="localhost",user="root",password="",database="company")
# cursor=con.cursor()
# sql="insert into t_dept values(%s,%s,%s)"
# #
# param=[50,'abc','北京']
#
# num=cursor.execute(sql,param)
# con.commit()
#
# print("影响了",num,"行数据")
#
# cursor.close()
# con.close()

# 删除
# con=pymysql.connect(host="localhost",user="root",password="",database="company")
# cursor=con.cursor()
# sql="delete from t_dept where deptno=%s"
# #
# param=[50]
#
# num=cursor.execute(sql,param)
# con.commit()
#
# print("影响了",num,"行数据")
#
# cursor.close()
# con.close()

# 更改
# con=pymysql.connect(host="localhost",user="root",password="",database="company")
# cursor=con.cursor()
# sql="update t_dept set dname=%s,loc=%s  where deptno=50 "
# #
# param=['aaa','上海']
#
# num=cursor.execute(sql,param)
# con.commit()
#
# print("影响了",num,"行数据")
#
# cursor.close()
# con.close()

# 查询
con=pymysql.connect(host="localhost",user="root",password="",database="company")
cursor=con.cursor()
sql="select * from t_dept where deptno=%s"

param=[50]

num=cursor.execute(sql,param)
data=cursor.fetchall()
con.commit()

print("影响了",num,"行数据")
for i in data:
    print(i)
cursor.close()
con.close()