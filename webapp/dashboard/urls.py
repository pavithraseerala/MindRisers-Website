from django.urls import path
from . import views

urlpatterns=[
    path('logincheck',views.logincheck,name='logincheck'),
    path('register_student_db',views.register_student_db,name='register_student_db'),
    path('register_teacher_db',views.register_teacher_db,name='register_teacher_db'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('teacher_dashboard',views.teacher_dashboard,name='teacher_dashboard'),
    path('profile_student',views.profile_student,name='profile_student'),
    path('profile_teacher',views.profile_teacher,name='profile_teacher'),
    path('book_tutor',views.book_tutor,name='book_tutor'),
    path('booking_confirmation',views.booking_confirmation,name='booking_confirmation'),
    path('paymentGateway',views.paymentGateway,name='paymentGateway'),
    path('chatapplication',views.chatapplication,name='chatapplication')
]