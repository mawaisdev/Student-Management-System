from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Creating class custom user and passing parent
# AbstractUser so we can Extend the Default Auth User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


# Create your models here.


class AdminHOD(models.Model):
    ID = models.AutoField(primary_key=True)
    Created_at = models.DateField(auto_now_add=True)
    Updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()
    # Here making oneToOneField relation Between User Model and HOD model
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Staffs(models.Model):
    ID = models.AutoField(primary_key=True)
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
    courseID = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
    staffID = models.ForeignKey(Staffs,on_delete=models.CASCADE)
    Created_at = models.DateField(auto_now_add=True)
    Updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()


class Students(models.Model):
    ID = models.AutoField(primary_key=True)
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
    studentID = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attandanceID = models.ForeignKey(Attandance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveReportStudent(models.Model):
    ID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
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
    studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
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
    studentID = models.ForeignKey(Students, on_delete=models.CASCADE)
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


# Creating @ receiver (post_save,sender=CustomUser)
# so this method Will Run only when data added in CustomUser
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance, courseID=Courses.objects.get(ID=1),
                                    session_start_year="2019-01-01", session_end_year="2023-01-01", Address="",
                                    Profile="", Gender="")


# now  @receiver (post_save, sender=CustomUser)
# def save_user_profile method will call after create user profile Execution

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, created, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()
