from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.user.first_name

class Student(models.Model):
    sign = models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    institute = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.sign.user.first_name

class Instructor(models.Model):
    sign = models.ForeignKey(Signup,on_delete=models.CASCADE,null=True)
    institute_name = models.CharField(max_length=100,null=True)
    institute_type = models.CharField(max_length=100,null=True)
    expect_student = models.IntegerField(null=True)
    purpose = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.sign.user.first_name

class Course(models.Model):
    instruct = models.ForeignKey(Instructor,on_delete=models.CASCADE,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.title+" "+self.instruct.sign.user.first_name


class Book(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    book_title = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.course.title+" "+self.book_title

class Book_Topic(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    topic_name = models.CharField(max_length=30,null=True)
    topic_file = models.FileField(null=True)
    def __str__(self):
        return self.topic_name

class Assignment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=30,null=True)
    question = models.CharField(max_length=250,null=True)
    publish_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    file = models.FileField(null=True)
    def __str__(self):
        return self.course.title+" "+ self.title

class Status2(models.Model):
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.status

class Submitted_Assignment(models.Model):
    status = models.ForeignKey(Status2,on_delete=models.CASCADE,null=True)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,null=True)
    submitted_by = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    marks = models.IntegerField(null=True)
    submit_date = models.DateField(null=True)
    file = models.FileField(null=True)
    def __str__(self):
        return self.assignment.course.title+" "+ self.assignment.title+" "+self.submitted_by.sign.user.first_name

class Status(models.Model):
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.status



class Enrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    date1 = models.DateField(null=True)
    def __str__(self):
        return self.course.title+"."+self.student.sign.user.first_name