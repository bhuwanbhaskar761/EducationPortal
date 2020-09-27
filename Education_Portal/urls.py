from django.contrib import admin
from django.urls import path
from education.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name="home"),
    path('about', About, name="about"),
    path('signup', Signup_Student, name="signup"),
    path('contact', Contact, name="contact"),
    path('admin_home', Admin_Home, name="admin_home"),
    path('login_user', Login, name="login_user"),
    path('login_admin', Admin_Login, name="login_admin"),
    path('logout', Logout, name="logout"),
    path('view_course', View_Course, name="view_course"),
    path('view_student', View_Student, name="view_student"),
    path('view_book', View_Book, name="view_book"),
    path('view_assignment', View_Assignment, name="view_assignment"),
    path('view_topic', View_Topic, name="view_topic"),
    path('course_user', Course_User, name="course_user"),
    path('view_instructor', View_Instructor, name="view_instructor"),
    path('signup_instructor', Signup_Instructor, name="signup_instructor"),
    path('instruct_home', Instruct_Home, name="instruct_home"),
    path('instructor_login', Instruct_Login, name="instructor_login"),
    path('view_course_instruct', View_Course_Instruct, name="view_course_instruct"),
    path('view_enroll_req', View_Enrollment_Req, name="view_enroll_req"),
    path('add_course', Add_Course, name="add_course"),
    path('add_topic', Add_Topic, name="add_topic"),
    path('my_dashboard', Dashboard, name="my_dashboard"),
    path('enroll/<int:pid>', Enrollment_Now, name="enroll"),
    path('course_section/<int:pid>', Course_Section, name="course_section"),
    path('assign_marks/<int:pid>', Assign_Marks, name="assign_marks"),
    path('assign_status/<int:pid>', Assign_Status, name="assign_status"),
    path('upload_assignment/<int:pid>', Upload_Assignment, name="upload_assignment"),
    path('delete_course/<int:pid>', delete_course, name="delete_course"),
    path('delete_instruct/<int:pid>', delete_instruct, name="delete_instruct"),
    path('delete_student/<int:pid>', delete_student, name="delete_student"),
    path('delete_topic/<int:pid>', delete_topic, name="delete_topic"),
    path('delete_book/<int:pid>', delete_book, name="delete_book"),
    path('delete_assign/<int:pid>', delete_assign, name="delete_assign"),
    path('delete_assign_submit/<int:pid>', delete_assign_submit, name="delete_assign_submit"),
    path('add_book', Add_Book, name="add_book"),
    path('add_assignment', Add_Assignment, name="add_assignment"),
    path('assignment_question', Assignment_Question, name="assignment_question"),
    path('profile', profile, name="profile"),
    path('instruct_profile', Instruct_profile, name="instruct_profile"),
    path('edit_profile', Edit_profile, name="edit_profile"),
    path('edit_profile_instruct', Edit_Instruct_profile, name="edit_profile_instruct"),
    path('change_password', Change_Password, name="change_password"),
    path('instruct_change_password', Instruct_Change_Password, name="instruct_change_password"),
    path('Total_Enrollment_Req', Total_Enrollment_Req, name="Total_Enrollment_Req")
]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)