from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from app01.models import * 

# 视图函数
# Create your views here.

def index(request):
    return HttpResponse('欢迎使用Django')
def index_niubi(request):
    return HttpResponse('宇宙无敌大帅哥 在此')
def user_list(request):
    #默认在app01/templates目录下找user_list.html（如果存在多个app，则会按照注册的顺序查找）
    return render(request,'user_list.html')
def template_test(request):
    #默认在app01/templates目录下找tpl.html
    name = "张三"
    roles=["admin","user","ceo"]
    user_info = {"name":"张三","age":18,'salary':9999,'role':'cto'}
    data_list = [{"name":"张三","age":18,'salary':9999,'role':'cto'},
                {"name":"李四","age":28,'salary':19999,'role':'ceo'},
                {"name":"王五","age":38,'salary':29999,'role':'hr'}
                ]
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":user_info,'n4':data_list})
def template_test2(request):
    #默认在app01/templates目录下找tpl.html
    name = "张三"
    roles=["admin","user","ceo"]
    data_list = [{"name":"张三","age":18,'salary':9999,'role':'cto'},
                {"name":"李四","age":28,'salary':19999,'role':'ceo'},
                {"name":"王五","age":38,'salary':29999,'role':'hr'}
                ]
    return render(request,'tpl2.html')

def weiliantongji(request):
    import requests 
    res = requests.get("http://www.baidu.com")
    data_list = res.json()
    
    return render(request,'news.html',{"data_list":data_list})

def request_something(request):
    #请求对象
    # print(request)#包含的用户请求的所有数据
    # #请求头
    # print(request.META)
    # #请求方法
    print(request.method) 
    print(request.GET)
    # #请求路径
    # print(request.path)
    # #请求参数
    # print(request.GET)
    # print(request.POST)
    # #请求体(使用post请求)
    # print(request.body)
    #响应对象
    #return HttpResponse('请求和响应')
    return redirect('http://www.baidu.com')#重定向
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
 
    #获取用户提交的数据
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    if user == 'admin' and pwd == '123':
        return redirect('http://www.baidu.com')

    return render(request,'login.html',{'msg':'用户名或密码错误'})

def orm(request):
    #增删改查
    #查询
    # UserInfo.objects.all()#查询所有
    # UserInfo.objects.filter(username='张三')#查询
    # UserInfo.objects.get(username='张三')#查询
    # UserInfo.objects.exclude(username='张三')#查询
    # UserInfo.objects.order_by('id')#排序
    # UserInfo.objects.order_by('-id')#排序
    # UserInfo.objects.first()#查询第一个
    # UserInfo.objects.last()#查询最后一个
    # UserInfo.objects.count()#查询数量
    # UserInfo.objects.values('id','username')#查询指定字段
    # UserInfo.objects.values_list('id','username')#查询指定字段
    # UserInfo.objects.create(username='张三',password='123',age=18)#新增
    # UserInfo.objects.filter(username='张三').update(age=20)#修改
    # UserInfo.objects.filter(username='张三').delete()#删除
    # UserInfo.objects.all().delete()#删除
    Department.objects.create(title='人事部')
    Department.objects.create(title='财务部')
    Department.objects.create(title='技术部')
    UserInfo.objects.create(username='张三',password='123',age=18)
    UserInfo.objects.create(username='李四',password='123',age=28)
    UserInfo.objects.filter(username='张三').update(age=20)
    #UserInfo.objects.filter(username='张三').delete()
    #UserInfo.objects.all().delete()
    #获取数据
    # user_list = UserInfo.objects.all()#queryset
    # for row in user_list:
    #     print(row.username,row.password,row.age)
    # data_list = UserInfo.objects.fliter(id=1)
    # row_obj = UserInfo.objects.fliter(id=1).first()
    ##更新数据
    # UserInfo.objects.filter(id=1).update(password=999)
    # UserInfo.objects.filter(name= "张三").update(age=30)
    return HttpResponse('orm操作执行成功')

def user_list(request):
    #1.获取数据库中所有的用户信息
    user_list = UserInfo.objects.all()
    # for item in user_list:
    #     print(item.id,item.username,item.password)
    # print(user_list)
    
    #return HttpResponse('orm操作执行成功')
    #渲染返回给用户
    return render(request,'user_info.html',{'user_list':user_list})
    #return render(request,'user_info.html')
    
def user_add(request):
    if request.method == 'GET':
        return render(request,'user_add.html')
    #获取用户提交的数据
    print(request.POST)
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    age = request.POST.get('age')
    #将数据添加到数据库中
    UserInfo.objects.create(username=user,password=pwd,age=age)
    return redirect('/info/list/')
def user_del(request):
    #获取用户提交的数据
    user_id = request.GET.get('nid')
    #删除数据
    UserInfo.objects.filter(id=user_id).delete()
    #return HttpResponse('删除成功')
    return redirect('/info/list/')