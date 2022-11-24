from django.urls import path
from . views import *

urlpatterns = [

    path('post/', PostView.as_view(), name = 'post_view'),
    # path("login/",views.loginform,name = "login"),
    # path("logout/",views.logout_profile,name = "logout"),
    # path("hrprofile/userprofile/<int:id>/",views.user_profile,name = "userprofile"),
    # path("hrprofile/",views.hr_profile,name = "hrprofile"),
    # path('hrprofile/delete/<int:id>/',views.delete,name = 'delete'),
    # path('hrprofile/userprofile/deleteatt/<int:id>',views.delete_att,name = 'deleteatt'),
    # path('hrprofile/userprofile/update/<int:id>',views.update,name = 'update'),
    # path("userpersonal/<int:id>/",views.user_personal,name = "userpersonal"),
    # path('userpersonal/add/',views.add,name = 'addrecord'),
    # path ('test/<int:id>/',views.test_vue, name = 'testvue'),

]
