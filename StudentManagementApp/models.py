from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Creating class custom user and passing parent
# AbstractUser so we can Extend the Default Auth User


class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


# Create your models here.


class AdminHOD(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Created_at = models.DateField(auto_now_add=True)
    Updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()
    # Here making oneToOneField relation Between User Model and HOD model
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Staffs(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Address = models.TextField()
    Created_at = models.DateField(auto_now_add=True)
    Updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()
    # Here making oneToOneField relation Between User Model and HOD model
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Courses(models.Model):
    ID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255)
    Created_at = models.DateField(auto_now_add=True)
    Updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()


class Subject(models.Model):
    ID = models.AutoField(primary_key=True)
    subjectName = models.CharField(max_length=255)
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    staffID = models.ForeignKey(Staffs,on_delete=models.CASCADE)
    Created_at = models.DateField(auto_now_add=True)
    Updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()


class Student(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Gender = models.CharField(max_length=20)
    Profile = models.FileField()
    Address = models.TextField()
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE)
    Created_at = models.DateField(auto_now_add=True)
    Updated_at = models.DateField(auto_now_add=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()
    # Here making oneToOneField relation Between User Model and HOD model
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Attandance(models.Model):
    ID = models.AutoField(primary_key=True)
    subjectID = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attandanceDate = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AttandanceReport(models.Model):
    ID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attandanceID = models.ForeignKey(Attandance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveReportStudent(models.Model):
    ID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    leaveDate = models.CharField(max_length=255)
    leaveMessage = models.TextField()
    leaveStatus = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class LeaveReportStaff(models.Model):
    ID = models.AutoField(primary_key=True)
    staffID = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leaveDate = models.CharField(max_length=255)
    leaveMessage = models.TextField()
    leaveStatus = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedbackStudent(models.Model):
    ID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedbackReply = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedbackStaff(models.Model):
    ID = models.AutoField(primary_key=True)
    staffID = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedbackReply = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStudent(models.Model):
    ID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStaff(models.Model):
    ID = models.AutoField(primary_key=True)
    staffID = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()
    leaveStatus = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()