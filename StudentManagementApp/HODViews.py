from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from StudentManagementApp.models import CustomUser, Staffs, Courses, Subject


def admin_home(request):
    return render(request, "HOD/home_content.html")

# ------------------------------------------------- Staff Section -----------------------------------

def add_staff(request):
    return render(request, "HOD/add_staff.html")


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        email = request.POST.get("email")
        try:
            user = CustomUser.objects.create_user(username=user_name, password=password, email=email,
                                                  first_name=first_name,
                                                  last_name=last_name, user_type=2)
            user.staffs.Address = address
            user.save()
        except:
            messages.error(request, "Failed to Add Staff")
            return HttpResponseRedirect("/add_staff")
        else:
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")


def manage_staff(request):
    pass
# ------------------------------------------------- Course Section ----------------------------------

def add_course(request):
    return render(request, "HOD/add_course.html")


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        try:
            course_name = request.POST.get("course_name")
            course = Courses(courseName=course_name)
            course.save()
        except:
            messages.error(request, "Failed to Add Course")
            return HttpResponseRedirect("/add_course")
        else:
            messages.success(request, "Course Added Successfully")
            return HttpResponseRedirect("/add_course")


# ------------------------------------------------- Student Section ---------------------------------
def add_student(request):
    courses = Courses.objects.all()
    return render(request, "HOD/add_student.html", {"courses": courses})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        email = request.POST.get("email")
        session_start_year = request.POST.get("session_start_date")
        session_end_year = request.POST.get("session_end_date")
        course_id = request.POST.get("course")
        Gender = request.POST.get("gender")

        try:
            user = CustomUser.objects.create_user(username=user_name, password=password, email=email,
                                                  first_name=first_name,
                                                  last_name=last_name, user_type=3)

            user.students.Address = address
            course_obj = Courses.objects.get(ID=course_id)
            user.students.courseID = course_obj
            user.students.session_start_year = session_start_year
            user.students.session_end_year = session_end_year
            user.students.Profile = ""
            user.students.Gender = Gender
            user.save()
        except:
            messages.error(request, "Failed to Add Student")
            return HttpResponseRedirect("/add_student")
        else:
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_student")


# ------------------------------------------------- Subject Section ---------------------------------
def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, "HOD/add_subject.html", {"staffs": staffs, "courses": courses})


def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(ID=course_id)
        s_id = request.POST.get("staffID")
        staff = CustomUser.objects.get(id=s_id)
        try:
            subject = Subject(subjectName=subject_name, courseID=course, staffID=staff)
            subject.save()
            messages.success(request, "Subject Added Successfully")
            return HttpResponseRedirect("/add_subject")
        except:
            messages.error(request, "Failed to Add Subject")
            return HttpResponseRedirect("/add_subject")
