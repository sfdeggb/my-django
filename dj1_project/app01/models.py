from django.db import models
#对数据库进行操作
# # Create your models here.

class UserInfo(models.Model):#表名
    #id
    #username
    #password
    #age
    username = models.CharField(max_length=32)#字段
    password = models.CharField(max_length=64)#字段
    age = models.IntegerField(default=2)#字段

class Department(models.Model):
    #id
    #name
    #create_time
    #update_time
    #is_delete
    title = models.CharField(max_length=26)
class Role(models.Model):
    #id
    #title
    #create_time
    #update_time
    #is_delete
    caption = models.CharField(max_length=26)

## 对数据进行增删改查
# ##########################新建数据############################
# # insert into app01_department(title) values('人事部')    
# Department.objects.create(title='人事部')

# # insert into app01_userinfo(username,password,age) values('张三','123',18)
# UserInfo.objects.create(username='张三', password='123', age=18)


