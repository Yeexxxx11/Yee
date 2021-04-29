import D_o
Try=D_o.Database_operation('students')
Try.select('select * from student')  # 查询所有记录
# Try.add("insert into student (stuName,stuSex,stuScore,stuAge) values ('Rose','女',57,19)")
Try.add("insert into student (stuName,stuSex,stuScore,stuAge) values ('Mary','女',90,19)")
Try.update("update student set stuScore=stuScore-5")
# Try.delete("delete from student where stuName='Mary'")
Try.delete("delete from student where stuName='Rose'")
Try.close()
