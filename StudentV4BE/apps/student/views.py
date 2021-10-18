import hashlib
import uuid

from django.shortcuts import render
from student.models import Student
# Create your views here.

from django.http import JsonResponse
import json
from django.db.models import Q
from django.conf import settings
import os

def get_students(request):
    """获取所有学生信息"""
    # 使用ORM获取所有学生信息
    try:
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "获取学生信息出现异常，具体错误：" + str(e)})
        # 如果出现异常返回


def query_students(request):
    # 接收传递过来的查询条件 -- axios默认json
    data = json.loads(request.body.decode('utf-8'))

    # 使用ORM获取所有满足条件的学生信息
    try:
        obj_students = Student.objects.filter(Q(sno__icontains=data['inputstr']) | Q(name__icontains=data['inputstr']) |
                                              Q(gender__icontains=data['inputstr']) | Q(
            mobile__icontains=data['inputstr'])
                                              | Q(email__icontains=data['inputstr']) | Q(
            address__icontains=data['inputstr'])).values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "查询学生信息出现异常，具体错误：" + str(e)})
        # 如果出现异常返回


def is_Exist_Sno(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_students = Student.objects.filter(sno=data['sno'])
        if obj_students.count() == 0:
            return JsonResponse({'code': 1, 'exist': False})
        else:
            return JsonResponse({'code': 1, 'exist': True})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '校验学号失败，具体原因是' + str(e)})


def add_Student(request):
    data = json.loads(request.body.decode('utf-8'))

    try:
        obj_student = Student(sno=data['sno'], name=data['name'], gender=data['gender'], birthday=data['birthday'],
                              mobile=data['mobile'], email=data['email'], address=data['address'])
        obj_student.save()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})

    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '添加到数据库出现异常,具体原因 ' + str(e)})


def update_Student(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_student = Student.objects.get(sno=data['sno'])
        # 依次修改
        obj_student.name = data['name']
        obj_student.gender = data['gender']
        obj_student.birthday = data['birthday']
        obj_student.mobile = data['mobile']
        obj_student.email = data['email']
        obj_student.address = data['address']
        # 保存
        obj_student.save()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})

    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '修改保存到数据库出现异常,具体原因 ' + str(e)})


def delete_Student(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        for one_student in data['student']:
            # 查询当前记录
            obj_student = Student.objects.get(sno=one_student['sno'])
            # 删除
            obj_student.delete()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})

    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '删除学生信息到数据库出现异常,具体原因 ' + str(e)})


def delete_Students(request):
    """批量删除学生信息"""
    # 接收前端传递过来的值
    data = json.loads(request.body.decode("utf-8"))
    try:
        # 遍历传递的集合
        for one_student in data['student']:
            # 查询当前记录
            obj_student = Student.objects.get(sno=one_student['sno'])
            # 执行删除
            obj_student.delete()
        # 使用ORM获取所有学生信息 并把对象转为字典格式
        obj_students = Student.objects.all().values()
        # 把外层的容器转为List
        students = list(obj_students)
        # 返回
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "批量删除学生信息写入数据库出现异常，具体原因：" + str(e)})


def upload(request):
    # 接收上传的文件
    rev_file = request.FILES.get('avatar')
    # 判断是否有文件
    if not rev_file:
        return JsonResponse({'code': 0, 'msg': '图片不存在'})
    new_name = get_random_str()
    # 准备写入的URL
    file_path = os.path.join(settings.MEDIA_ROOT, new_name+os.path.splitext(rev_file.name)[1])
    # 开始写入磁盘
    try:
        f = open(file_path,'wb')
        # 多次写入
        for i in rev_file.chunks():
            f.write(i)
        # 要关闭
        f.close()
        # 返回
        return JsonResponse({'code': 1, 'name': new_name + os.path.splitext(rev_file.name)[1]})

    except Exception as e:
        return JsonResponse({'code':0, 'msg':str(e)})



def get_random_str():
    #获取uuid的随机数
    uuid_val = uuid.uuid4()
    #获取uuid的随机数字符串
    uuid_str = str(uuid_val).encode('utf-8')
    #获取md5实例
    md5 = hashlib.md5()
    #拿取uuid的md5摘要
    md5.update(uuid_str)
    #返回固定长度的字符串
    return md5.hexdigest()
