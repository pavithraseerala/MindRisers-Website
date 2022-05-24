from django.urls import path
from . import views

urlpatterns=[
    path('',views.baseHome,name='baseHome'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('register_student',views.register_student,name='register-student'),
    path('register_teacher',views.register_teacher,name='register-teacher'),
    path('register_student_db',views.register_student_db,name='register_student_db'),
    path('register_teacher_db',views.register_teacher_db,name='register_teacher_db'),
    path('logincheck',views.logincheck,name='logincheck')
    
]