 # -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.db import connections
from django.http import HttpResponse,JsonResponse

def index(request):

    return render(request,'login.html')



#..-------------------------------
# def regist(request):
#
#     sign_id = request.GET.get('sign_id')
#     sign_pw = request.GET.get('sign_pw')
#     sign_name = request.GET.get('sign_name')
#
#     lock = 0
#     print sign_id
#     print sign_pw
#     print sign_name
#
#     with connections['default'].cursor() as cur:
#             query = '''
#                 select id from login
#                 where id = '{id}'
#             '''.format(id=sign_id)
#             cur.execute(query)
#             rows = cur.fetchall()
#
#     if len(rows) != 0:
#
#         lock = 1
#         return JsonResponse({'return':'fail'})
#
#     with connections['default'].cursor() as cur:
#             query = '''
#                 insert into login(id, password, name)
#                 values('{id}',MD5('{password}'),'{name}')
#             '''.format(id=sign_id,password=sign_pw,name=sign_name,)
#             cur.execute(query)
#
#             print query
#
#     return JsonResponse({'return':'success', 'id':sign_id, 'password':sign_pw,'name':sign_name})
#
# def Home(request):
#
#     #print request.session.get('user_id')
#
#     if 'user_id' not in request.session:  #id 를 생성해서 들어간 페이지가 아닐경우 session 존재하지 않으니 return
#
#         return render (request ,'error.html')  # Sesseion 없어서 return 된 경우   ->error.html
#
#     return render (request ,'Home.html')

# ----------------------------------------------