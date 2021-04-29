import pymysql

class Database_operation(object):
    def __init__(self,database):
        self.conn = pymysql.connect(host='127.0.0.1', database=database, user='root', password='123456', charset='utf8')
        self.cursor=self.conn.cursor()

    def select(self,sql):
        try:
            result = self.cursor.execute(sql)
            print(result)
            print(self.cursor.fetchall())
        except:
            print("操作失败！")
            self.conn.rollback()


    def add(self, sql):
        try:
            result = self.cursor.execute(sql)
            print(result)
            self.conn.commit()
        except:
            print("操作失败！")
            self.conn.rollback()

    def delete(self,sql):
        try:
            result = self.cursor.execute(sql)
            print(result)
            self.conn.commit()
        except:
            print("操作失败！")
            self.conn.rollback()

    def update(self,sql):
        try:
            result = self.cursor.execute(sql)
            print(result)
            self.conn.commit()
        except:
            print("操作失败！")
            self.conn.rollback()


    def close(self):
        self.cursor.close()
        self.conn.close()




# Try=Database_operation('students')
# Try.select('select * from student')  # 查询所有记录
# Try.add("insert into student (stuName,stuSex,stuScore,stuAge) values ('Rose','女',57,19)")
# Try.add("insert into student (stuName,stuSex,stuScore,stuAge) values ('Mary','女',90,19)")
# Try.update("update student set stuScore=stuScore-5")
# Try.delete("delete from student where stuName='Mary'")
# Try.close()

