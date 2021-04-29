# 1、创建数据库的连接对象(connection)
# 2、创建游标对象（cursor）
# 3、使用游标对象，执行sql语句（execute）,判断是否执行成功？
#     如果执行成功，则执行提交操作（commmit），数据库里的数据才会改变;否则执行回滚操作（rollback）
# 4、关闭游标，关闭连接（close）
import pymysql
conn = pymysql.connect(host='127.0.0.1',database='students',user='yourusername',password='yourpassword',charset='utf8')
cursor = conn.cursor()
#增
sql="insert into student (stuName,stuSex,stuScore,stuAge) values('Rose','女',57,19) "
# 删
# sql="delete from student where stuName='Tom'"
# 改
# sql="update student set stuAge=stuAge+1 where stuSex='男' "
# 查
# sql='select * from student'  # 查询所有记录
# sql='select stuName from student'  # 查询名字
# sql='select * from student where stuScore>=60'  #查询成绩大于60的学生成绩
try:
    result = cursor.execute(sql)
    print(result)
    # print(cursor.fetchall())
    # conn.commit()
except:
    print("操作失败！")
    conn.rollback()

cursor.close()
conn.close()