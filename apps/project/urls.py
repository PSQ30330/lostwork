from django.conf.urls import url

from project import views

urlpatterns =[
    url(r'^add_projet/$',views.add_project,name="添加实训题目"),
    url(r'^info/$',views.info,name="学生选题"),
    url(r'^select/$',views.select_project,name="houduan"),
    url(r'^xuanti/',views.student_xunti,name ="选题"),
    url(r'^chakan/$',views.chakan,name="查看选题"),
    url(r'^stu_chakan/$',views.stu_chakan,name="返回题目"),
    url(r'^test/$',views.select_situation,name='刷新选题情况'),
    url(r'^data/$',views.teacher_chakan,name='查看已经选题学生'),
    url(r'^data_not/$',views.tea_chakan,name='查看未选题学生'),
    url(r'^tea_chakan/$',views.chakan_select,name="查看学生已选题"),
    url(r'^tea_chakannot/$',views.chakan_notok,name='查看未选题情况'),
    url(r'^count/$',views.kaohe),
    url(r'^chakancount/$',views.chakan_count),
    url(r'^chacount/$',views.cha_count),
    url(r'^(?P<pk>\d+)/$',views.project_page,name = 'page'),
    url(r'^shixun/',views.shuxun),



]