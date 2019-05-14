from django.db import transaction
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from comment import models


@csrf_exempt
def comment(request):
    if request.method == 'POST':

        res = {'code': 0}
        pro_id = request.POST.get('pro_id')

        username = request.POST.get('username')

        content = request.POST.get('content')

        parent_id = request.POST.get("parent_id")

        with transaction.atomic():
            if parent_id:

                comment_dic = models.Comment.objects.create(pro_id=pro_id, username=username, content=content,parent_id=parent_id)
                res['data'] = {
                    'parent_id': comment_dic.parent_id,
                    'id': comment_dic.pro_id,
                    'username': comment_dic.parent_comment.username,
                    'content': comment_dic.content,
                    'parent_comment_content':comment_dic.parent_comment_content.content,
                    'create_time': comment_dic.c_time.strftime("%Y-%m-%d %H:%M:%S")}


            else:
                comment_dic = models.Comment.objects.create(pro_id=pro_id, username=username, content=content)



                res['data']= {
                    'parent_id': comment_dic.parent_id,
                    'id': comment_dic.pro_id,
                    'username': comment_dic.username,
                    'content': comment_dic.content,

                    'create_time': comment_dic.c_time.strftime("%Y-%m-%d %H:%M:%S") }


        return JsonResponse(res)

