from django.shortcuts import render
from student.models import Student
# Create your views here.

from django.http import JsonResponse
import json
from django.db.models import Q


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
        
        obj_student.save()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})

    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '添加到数据库出现异常,具体原因 ' + str(e)})
