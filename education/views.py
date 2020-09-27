from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import datetime
from .models import *
# Create your views here.
def Home(request):
    return render(request,'user_home.html')

def Instruct_Home(request):
    course=0
    student=0
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    instruct = Instructor.objects.get(sign=sign)
    enroll = Enrollment.objects.all()
    cou = Course.objects.filter(instruct=instruct)
    for i in cou:
        course+=1
    for i in enroll:
        if i.course.instruct.id == instruct.id:
            student+=1
    d ={'student':student,'course':course}
    return render(request,'instruct_home.html',d)


def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')


def Signup_Student(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        i = request.FILES['image']
        p = request.POST['pwd']
        inst = request.POST['institute']
        con = request.POST['contact']
        user = User.objects.create_user(username=u, password=p, first_name=f,last_name=l)
        sign = Signup.objects.create(user=user,contact=con,image=i)
        Student.objects.create(sign=sign,institute=inst)
        error = True
    d = {'error':error}
    return render(request, 'signup.html',d)

def Signup_Instructor(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        i = request.FILES['image']
        p = request.POST['pwd']
        inst = request.POST['institute']
        inst_type = request.POST['inst_type']
        pur = request.POST['purpose']
        ex = request.POST['expect']
        con = request.POST['contact']
        user = User.objects.create_user(username=u, password=p, first_name=f,last_name=l)
        sign = Signup.objects.create(user=user,contact=con,image=i)
        Instructor.objects.create(sign=sign,institute_name=inst,institute_type=inst_type,expect_student=ex,purpose=pur)
        error = True
    d = {'error':error}
    return render(request, 'signup_instruct.html',d)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "yes"
        else:
            error = "not"
    d = {'error': error}
    return render(request,'login.html',d)


def Instruct_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "yes"
        else:
            error = "not"
    d = {'error': error}
    return render(request,'istructor_login.html',d)

def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'loginadmin.html',d)


def Logout(request):
    logout(request)
    return redirect('home')

def Admin_Home(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    sign=""
    data1 = Student.objects.all()
    data2 = Instructor.objects.all()
    data3 = Course.objects.all()
    student =0
    instruct = 0
    course = 0
    for i in data1:
        student+=1
    for i in data2:
        instruct+=1
    for i in data3:
        course+=1

    d = {'student':student,'instruct':instruct,'course':course}
    return render(request,'admin_home.html',d)

def View_Instructor(request):
    pro = Instructor.objects.all()
    d = {'pro': pro}
    return render(request,'view_instructor.html',d)

def View_Student(request):
    pro = Student.objects.all()
    d = {'pro': pro}
    return render(request,'view_student.html',d)

def View_Course(request):
    pro = Course.objects.all()
    d = {'pro': pro}
    return render(request,'view_course.html',d)

def View_Book(request):
    pro = Book.objects.all()
    d = {'pro': pro}
    return render(request,'view_book.html',d)

def View_Topic(request):
    pro = Book_Topic.objects.all()
    d = {'pro': pro}
    return render(request,'view_topic.html',d)

def View_Assignment(request):
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    instruct = Instructor.objects.get(sign=sign)
    pro = Submitted_Assignment.objects.all()
    d = {'pro': pro,'instruct':instruct}
    return render(request,'view_assignment.html',d)

def View_Enrollment_Req(request):
    pro = Enrollment.objects.all()
    d = {'pro': pro}
    return render(request,'view_enroll_req.html',d)
def Total_Enrollment_Req(request):
    pro = Enrollment.objects.all()
    d = {'pro': pro}
    return render(request,'enrolled_student.html',d)

def View_Course_Instruct(request):
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    instruct1 = Instructor.objects.get(sign=sign)
    pro = Course.objects.filter(instruct=instruct1)
    d = {'pro': pro}
    return render(request,'view_course_instruct.html',d)


def Course_User(request):
    pro = Course.objects.all()
    d = {'pro': pro}
    return render(request,'course_user.html',d)

def Add_Course(request):
    error = False
    if request.method=="POST":
        c = request.POST['course']
        s =  request.POST['date1']
        e = request.POST['date2']
        i = request.FILES['image']
        user = User.objects.get(id = request.user.id)
        sign = Signup.objects.get(user=user)
        instruct = Instructor.objects.get(sign=sign)
        Course.objects.create(instruct=instruct,title=c,start_date=s,end_date=e,image=i)
        error = True
    d = {'error':error}
    return render(request,'add_course.html',d)

def Add_Topic(request):
    error = False
    book = Book.objects.all()
    if request.method=="POST":
        c = request.POST['course']
        s =  request.POST['topic_name']
        e = request.FILES['file']
        course1 = Book.objects.get(book_title=c)
        Book_Topic.objects.create(topic_name=s,book=course1,topic_file=e)
        error = True
    d = {'error':error,'book':book}
    return render(request,'add_topic.html',d)

def Add_Book(request):
    error = False
    course = Course.objects.all()
    if request.method=="POST":
        c = request.POST['course']
        b =  request.POST['book_title']
        course1 = Course.objects.get(title=c)
        Book.objects.create(course=course1,book_title=b)
        error = True
    d = {'error':error,'course':course}
    return render(request,'add_book.html',d)

def Add_Assignment(request):
    error = False
    course = Course.objects.all()
    student = Student.objects.all()
    if request.method=="POST":
        c = request.POST['course']
        t =  request.POST['assign_title']
        d =  request.POST['desc']
        p =  request.POST['date1']
        e =  request.POST['date2']
        a = request.FILES['file']
        course1 = Course.objects.get(title=c)
        assign = Assignment.objects.create(title=t,course=course1,file=a,question=d,publish_date=p,end_date=e)
        for i in student:
            status = Status2.objects.get(status='NotSubmitted')
            Submitted_Assignment.objects.create(assignment=assign,submitted_by=i,status=status)
        error = True
    d = {'error':error,'course':course}
    return render(request,'add_assignment.html',d)

def Enrollment_Now(request,pid):
    course = Course.objects.get(id=pid)
    error = ""
    if request.method =="POST":
        user = User.objects.get(id=request.user.id)
        sign = Signup.objects.get(user=user)
        student = Student.objects.get(sign=sign)
        enroll1 = False
        try:
            enroll1 = Enrollment.objects.filter(student=student,course=course).first()
        except:
            pass
        if enroll1:
            error="already"
        else:
            sta = Status.objects.get(status="pending")
            Enrollment.objects.create(date1=datetime.date.today(),course=course,student=student,status=sta)
            error = "create"
    d = {'course':course,'error':error}
    return render(request,'enroll.html',d)

def Dashboard(request):
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    student = Student.objects.get(sign=sign)
    enroll = Enrollment.objects.filter(student=student)
    d = {'enroll':enroll}
    return render(request,'my_dashboard.html',d)

def Course_Section(request,pid):
    course = Course.objects.get(id=pid)
    book = Book.objects.filter(course=course)
    topic = Book_Topic.objects.all()
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    student = Student.objects.get(sign=sign)
    assign = Assignment.objects.filter(course=course).first()
    submit=Submitted_Assignment.objects.filter(submitted_by=student)
    d = {'assign':submit,'course':course,'book':book,'topic':topic}
    return render(request,'course_section1.html',d)

def multimedia(request,pid):
    course = Course.objects.get(id=pid)
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    student = Student.objects.get(sign=sign)
    assign = Assignment.objects.filter(course=course)
    d = {'assign':assign}
    return render(request,'assignment.html',d)

def Upload_Assignment(request,pid):
    assign = Submitted_Assignment.objects.get(id=pid)
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    student = Student.objects.get(sign=sign)
    error = ""
    if request.method=="POST":
        i = request.FILES['file1']
        status1 = Status2.objects.get(status="Submitted")
        assign.status = status1
        assign.file = i
        assign.submit_date = datetime.date.today()
        assign.save()
        error="create"
    d = {'error':error,'assign':assign}
    return render(request,'upload_assignment.html',d)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    student = Student.objects.get(sign=sign)

    d={'pro':student,'user':user}
    return render(request,'profile.html',d)

def Instruct_profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    user = User.objects.get(id=request.user.id)
    sign = Signup.objects.get(user=user)
    student = Instructor.objects.get(sign=sign)
    d={'pro':student,'user':user}
    return render(request,'instruct_profile.html',d)


def Edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error = False
    user=User.objects.get(id=request.user.id)
    pro = Signup.objects.get(user=user)
    student = Student.objects.get(sign=pro)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        i = request.POST['institute']
        try:
            fi = request.FILES['file']
            pro.image = fi
            pro.save()
        except:
            pass
        con = request.POST['contact']
        pro.user.username=u
        user.first_name=f
        user.last_name=l
        pro.contact=con
        student.institute = i
        pro.save()
        pro.user.save()
        user.save()
        student.save()
        error = True
    d = {'error':error,'pro':pro,'student':student}
    return render(request, 'edit_profile.html',d)

def Edit_Instruct_profile(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error = False
    user=User.objects.get(id=request.user.id)
    pro = Signup.objects.get(user=user)
    student = Instructor.objects.get(sign=pro)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        i = request.POST['institute']
        ins = request.POST['institute_type']
        pur = request.POST['purpose']
        try:
            fi = request.FILES['file']
            pro.image = fi
            pro.save()
        except:
            pass
        con = request.POST['contact']
        pro.user.username=u
        user.first_name=f
        user.last_name=l
        pro.contact=con
        student.institute_name = i
        student.institute_type = ins
        student.purpose = pur
        pro.save()
        pro.user.save()
        user.save()
        student.save()
        error = True
    d = {'error':error,'pro':pro,'student':student}
    return render(request, 'edit_profile_instruct.html',d)

def Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'change_password.html',d)

def Instruct_Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'change_password_instruct.html',d)

def Assign_Marks(request,pid):
    submit = Submitted_Assignment.objects.get(id=pid)
    error = False
    if request.method=="POST":
        a = request.POST['marks']
        submit.marks = a
        submit.save()
        error = True
    d = {'error':error}
    return render(request,'assign_marks.html',d)

def Assign_Status(request,pid):
    submit = Enrollment.objects.get(id=pid)
    assign = Assignment.objects.filter(course=submit.course.id)
    for i in assign:
        status = Status2.objects.get(status='NotSubmitted')
        submit2 = Submitted_Assignment.objects.filter(submitted_by=submit.student)
        if not submit2:
            Submitted_Assignment.objects.create(status=status, assignment=i, submitted_by=submit.student)

    status = Status.objects.all()
    error = False
    if request.method=="POST":
        a = request.POST['status']
        stats = Status.objects.get(status = a)
        submit.status = stats
        submit.save()
        error = True
    d = {'error':error,'status':status}
    return render(request,'assign_status.html',d)

def Assignment_Question(request):
    assign = Assignment.objects.all()
    d = {'pro':assign}
    return render(request,'assignment_question.html',d)

def delete_course(request,pid):
    cour = Course.objects.get(id=pid)
    cour.delete()
    if request.user.is_staff:
        return redirect('view_course')
    else:
        return redirect('view_course_instruct')



def delete_book(request,pid):
    cour = Book.objects.get(id=pid)
    cour.delete()
    return redirect('view_book')


def delete_student(request,pid):
    cour = Student.objects.get(id=pid)
    cour.delete()
    return redirect('view_student')

def delete_instruct(request,pid):
    cour = Instructor.objects.get(id=pid)
    cour.delete()
    return redirect('view_iinstructor')

def delete_topic(request,pid):
    cour = Book_Topic.objects.get(id=pid)
    cour.delete()
    return redirect('view_topic')

def delete_assign(request,pid):
    cour = Assignment.objects.get(id=pid)
    cour.delete()
    return redirect('assignment_question')

def delete_assign_submit(request,pid):
    cour = Submitted_Assignment.objects.get(id=pid)
    cour.delete()
    return redirect('view_assignment')