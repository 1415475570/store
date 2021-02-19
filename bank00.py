import random
import pymysql
# 银行的名称
bank_name = "北京市工商银行昌平支行"

# 银行的库
users = {
}
'''
{"张三":
    {account:"12345",
    password:"123456"}
},
{"李四"：
    {account："5868495",
    password:"654321"
    }
}

'''

# 欢迎界面
welcome  = '''
*********************************
*    欢迎来到中国工商银行管理系统 *
*********************************
*    1.开户                      *
*    2.存钱                      *
*    3.取钱                      *
*    4.转账                      *
*    5.查询                      *
*    6.bye！                     *
*********************************
'''



def bank():
    f=open("bank_users.txt","w+",encoding="utf-8")
    # account,username,password,money,country,province,street,door
    for key in users.keys():
        string=""
        string=string+key+","
        string=string+users[key]["account"]+","
        # string=string+users[key]["username"]+",",
        string=string+users[key]["password"]+","
        string = string + str(users[key]["money"]) + ","
        string = string + users[key]["country"] + ","
        string = string + users[key]["province"] + ","
        string = string + users[key]["street"] + ","
        string = string + users[key]["door"]
        f.write(string+"\n")
    f.closed




# 专门来获取8位随机账号
def getRandom():
    li = [1,2,3,4,5,6,7,8,9,0]
    # 循环8次
    string = ""
    for i in range(8): # 循环8次获取随机字符
        ch = li[random.randint(0,9)]
        string = string + str(ch)
    return string

# 银行的核心开户方法
def bank_mysql_insert(account,username,password,money,country,province,street,door):
    con = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cursor = con.cursor()
    sql="select  count(username) from users"
    cursor.execute(sql)
    data = cursor.fetchall()
    data1=data[0][0]
    if int(data1) <= 100:
        sql = "select username from users where username=%s"
        param=[username]
        cursor.execute(sql, param)
        data0=cursor.fetchall()
        if data0==0:
            sql = "insert into users values(%s,%s,%s,%s,%s,%s,%s,%s)"
            param = [account, username, password, money, country, province, street, door]
            num = cursor.execute(sql, param)
            con.commit()
            cursor.close()
            con.close()
            return 1
        else:
            return 2
    else:
        return 3

# 普通的开户方法
def addUser():
    # 完成具体的开户输入
    # 姓名(str)、密码(int:6位数字)、地址、存款余额(int)、国家(str)、省份(str)、街道(str)、门牌号(str)
    username = input("请输入姓名：")
    password = input("请输入初始取款密码：")
    money =  int(input("请输入您的初始金额：")) # 金额是整数形式
    print("接下来输入地址信息：")
    country =  input("请输入您所在国家：")
    province = input("请输入您所在省份：")
    street = input("请输入您所在的街道：")
    door = input("请输入您地址的门牌号：")
    account =  getRandom() # 获取随机账号

    # 将数据传给银行
    status = bank_mysql_insert(account,username,password,money,country,province,street,door)
    if status == 3:
        print("对不起，银行用户已满！请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请勿重复开户！")
    elif status == 1:
        print("恭喜，开户成功！以下是您的个人开户信息：")
        print("-------------------------------------")
        print("您的账号为:", users[username]["account"])
        print("您的余额为:", users[username]["money"])
        print("您的用户名为:", username)
        print("您所在国家为:", users[username]["country"])
        print("您所在省份为:", users[username]["province"])
        print("您所在街道为:", users[username]["street"])
        print("您所在门牌号为:", users[username]["door"])
        print("开户行名为:", users[username]["bank_name"])


# 银行的核心存款方法
def bank_savemoney(username, money):
    con=pymysql.connect(host="localhost",user="root",password="",database="bank")
    cursor=con.cursor()
    sql = "select * from users where username=%s"
    param = [username]
    num=cursor.execute(sql, param)
    data= cursor.fetchall()
    if num == 1:
        data0 = data[0][3]
        new_money=data0+money
        sql = "update users set money=%s where username=%s"
        param = [new_money,username]
        cursor.execute(sql, param)
        con.commit()
        cursor.close()
        con.close()
        print("存钱成功！！！您当前的余额为：",new_money,"元")
        return 1
    else:
        return 2

def savemoney():
    username = input("请输入用户名:")
    while True:
        money = input("请输入金额:")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("余额输入错误，请重新输入！")
    returnvalue = bank_savemoney(username, money)
    if returnvalue == 1:
        print("")
    else:
        print("查无此用户！！！")



# 银行的核心取款方法
def bank_mysql_update0(username,password,money):
    con=pymysql.connect(host="localhost",user="root",password="",database="bank")
    cursor=con.cursor()
    sql="select * from users where username=%s and password=%s"
    param=[username,password]
    num=cursor.execute(sql,param)
    data=cursor.fetchall()
    if num==1:
        new_data=data[0][3]
        if int(new_data)<money:
            return 3
        else:
            new_money=new_data-money
            sql="update users set money=%s where username=%s"
            param=[new_money,username]
            cursor.execute(sql,param)
            con.commit()
            cursor.close()
            con.close()
            print("取款成功！您的当前余额为：",new_money)
    elif num==0:
        sql= "select * from users where username=%s"
        param = [username]
        num=cursor.execute(sql, param)
        con.commit()
        cursor.close()
        con.close()
        if num==1:
            return 2
        else:
            return 1

def withdraw_money():
    username = input("请输入账号：")
    password = input("请输入取款密码：")
    money = int(input("请输入您的取款金额："))
    # 将数据传给银行
    status1=bank_mysql_update0(username,password,money)
    if status1==1:
        print("您输入的账号不存在！")
    elif status1==2:
        print("您输入的密码错误！")
    elif status1==3:
        print("您的余额不足！")



# 银行核心转账
def bank_transfer(out_username, in_username, out_pwd, out_money):
    con = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cursor = con.cursor()
    sql = "select username from users where username=%s"
    param1 = [out_username]
    num1 = cursor.execute(sql, param1)
    con.commit()
    cursor.close()
    con.close()

    con = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cursor = con.cursor()
    sql = "select username from users where username=%s"
    param2 = [in_username]
    num2 = cursor.execute(sql, param2)
    con.commit()
    cursor.close()
    con.close()

    if num1==1 and num2==1:
        con = pymysql.connect(host="localhost", user="root", password="", database="bank")
        cursor = con.cursor()
        sql = "select password from users where username=%s"
        param = [out_username]
        cursor.execute(sql,param)
        data=cursor.fetchall()
        data1=data[0][0]
        con.commit()
        cursor.close()
        con.close()
        if int(data1)==int(out_pwd):
            con = pymysql.connect(host="localhost", user="root", password="", database="bank")
            cursor = con.cursor()
            sql = "select money from users where username=%s"
            param = [out_username]
            cursor.execute(sql, param)
            data = cursor.fetchall()
            data2 = data[0][0]
            con.commit()
            cursor.close()
            con.close()
            if data2>=out_money:
                con = pymysql.connect(host="localhost", user="root", password="", database="bank")
                cursor = con.cursor()
                sql = "select money from users where username=%s"
                param = [in_username]
                num = cursor.execute(sql, param)
                data = cursor.fetchall()
                data3 = data[0][0]
                con.commit()
                cursor.close()
                con.close()
                data2=data2-out_money
                data3=data3+out_money

                con = pymysql.connect(host="localhost", user="root", password="", database="bank")
                cursor = con.cursor()
                sql = "update users set money=%s where username=%s"
                param = [data2,out_username]
                cursor.execute(sql, param)
                con.commit()
                cursor.close()
                con.close()

                con = pymysql.connect(host="localhost", user="root", password="", database="bank")
                cursor = con.cursor()
                sql = "update users set money=%s where username=%s"
                param = [data3, in_username]
                cursor.execute(sql, param)
                con.commit()
                cursor.close()
                con.close()

                print("转账成功！", "转出账号为:", out_username, "转出账号余额为:", data2, "转入账号为:",in_username,
                      "转入账号余额为:", data3)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def transferMoney():
    out_username = input("请输入转出账号:")
    in_username = input("请输入转入账号:")
    out_pwd = input("请输入转出账号密码:")
    out_money = int(input("请输入转出的金额:"))

    status5 = bank_transfer(out_username, in_username, out_pwd, out_money)
    if status5 == 1:
        print("转出账户或转入账户不存在！")
    elif status5 == 2:
        print("密码不正确！")
    elif status5 == 3:
        print("余额不足！")
    elif status5 == 0:
        print("")


# 银行查询
def query():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    savequery = bank_query(username, password)
    if savequery == 1:
        print()
    elif savequery == 2:
        print("密码输入错误")
    else:
        print("该用户不存在")

def bank_query(username, password):
    con = pymysql.connect(host="localhost", user="root", password="", database="bank")
    cursor = con.cursor()
    sql = "select * from users where username=%s and password=%s"
    param = [username,password]
    num = cursor.execute(sql, param)
    data=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    if num==1:
        print(data)
        return 1
    elif num==0:
        con = pymysql.connect(host="localhost", user="root", password="", database="bank")
        cursor = con.cursor()
        sql = "select * from users where username=%s"
        param = [username]
        num = cursor.execute(sql, param)
        con.commit()
        cursor.close()
        con.close()
        if num==1:
            return 2
    elif num==0:
        con = pymysql.connect(host="localhost", user="root", password="", database="bank")
        cursor = con.cursor()
        sql = "select * from users where username=%s"
        param = [username]
        num = cursor.execute(sql, param)
        con.commit()
        cursor.close()
        con.close()
        if num == 0:
            return 3


while True:
    print(welcome) # 打印欢迎信息
    chose = input("请输入您的业务编号：")
    if chose == "1":
        addUser()
        bank()
    elif chose == "2":
        savemoney()
        bank()
    elif chose == "3":
        withdraw_money()
        bank()
    elif chose == "4":
        transferMoney()
        bank()
    elif chose == "5":
        print("查询个人信息！")
        query()
        bank()
    elif chose  == "6":
        print("退出成功！欢迎下次光临！")
        break
    else:
        print("输入非法！请重新输入！")






