#1.导入pymysql代码库
import pymysql

def connDB():
   #我们想要链接数据库，需要知道数据库的哪些信息呢？？
   #ip地址，端口号，用户名户名和密码，数据库名称。。。
   conn=pymysql.Connect(host="localhost", user="root", password="root",database="pirate", port=3306,charset='utf8')
   #查询hd_user表中所有数据，倒叙打印
   sql="select * from hd_user order by id desc"
   #要想在代码中执行这条sql语句，首先你要获得数据库的游标cursor
   curs=conn.cursor()
   #通过游标执行sql语句
   curs.execute(sql)
   #想获取数据库中最新的记录，
   # 那么就要把数据库所有记录倒叙排列
   # 然后fetchone（）方法获取第一条记录，即数据库最新记录
   result=curs.fetchone()
   #如果想获取所有的查询结果，fetchall（）
   #result=curs.fetchall()
   return result

if __name__ == '__main__':
    connDB()
    print(connDB())