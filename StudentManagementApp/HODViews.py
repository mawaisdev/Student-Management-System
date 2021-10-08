from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from StudentManagementApp.models import CustomUser, Staffs, Courses, Subject, Students


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
    staffs = Staffs.objects.all()
    return render(request, "HOD/manage_staff.html", {"staffs": staffs})

# Here in this function i added two parameters ( first default request, staff_id from url )


def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request, "HOD/edit_staff.html", {"staff": staff, "id": staff_id})


def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        staff = CustomUser.objects.get(id=staff_id)
        staff_model = Staffs.objects.get(admin=staff_id)
        try:
            staff.first_name = first_name
            staff.last_name = last_name
            staff.email = email
            staff.username = username
            staff.save()

            staff_model.Address = address
            staff_model.save()
            messages.success(request, "Successfully Modified Staff")
            return HttpResponseRedirect("/edit_staff/"+staff_id)
        except:
            messages.error(request, "Failed to Modify Staff")
            return HttpResponseRedirect("/edit_staff/" + staff_id)
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
            messages.success(request, "Course Added Successfully")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed to Add Course")
            return HttpResponseRedirect("/add_course")


def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "HOD/manage_course.html", {"courses": courses})


def edit_course(request, course_id):
    course = Courses.objects.get(ID=course_id)
    return render(request, "HOD/edit_course.html", {"course": course, "id": course_id})


def edit_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not allowed")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course_name")
        try:
            course = Courses.objects.get(ID=course_id)
            course.courseName = course_name
            course.save()
            messages.success(request, "Course Updated Successfully")
            return HttpResponseRedirect("/edit_course/"+str(course.ID))
        except:
            messages.error(request, "Failed to Update Course")
            return HttpResponseRedirect("/edit_course/"+str(course.ID))

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
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=user_name, password=password, email=email,
                                                  first_name=first_name,
                                                  last_name=last_name, user_type=3)

            user.students.Address = address
            course_obj = Courses.objects.get(ID=course_id)
            user.students.courseID = course_obj
            user.students.session_start_year = session_start_year
            user.students.session_end_year = session_end_year
            user.students.Profile = profile_pic_url
            user.students.Gender = Gender
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to Add Student")
            return HttpResponseRedirect("/add_student")


def manage_student(request):
    students = Students.objects.all()
    return render(request, "HOD/manage_student.html", {"students": students})


def edit_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    courses = Courses.objects.all()

    return render(request, "HOD/edit_student.html", {"student": student, "courses": courses, "id": student_id})


def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        student_id = request.POST.get("studentID")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        address = request.POST.get("address")
        email = request.POST.get("email")
        session_start_year = request.POST.get("session_start_date")
        session_end_year = request.POST.get("session_end_date")
        course_id = request.POST.get("course")
        Gender = request.POST.get("gender")
        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            student = Students.objects.get(admin=student_id)
            student.Address = address
            student.session_start_year = session_start_year
            student.session_end_year = session_end_year
            student.Gender = Gender
            if profile_pic_url is not None:
                student.Profile = profile_pic_url

            course = Courses.objects.get(ID=course_id)
            student.courseID = course
            student.save()
            messages.success(request, "Successfully Updated Student")
            return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.error(request, "Failed to Update Student")
            return HttpResponseRedirect("/add_student/"+student_id)


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


def manage_subject(request):
    subjects = Subject.objects.all()
    return render(request, "HOD/manage_subject.html", {"subjects": subjects})


def edit_subject(request, subject_id):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    subject = Subject.objects.get(ID=subject_id)
    return render(request, "HOD/edit_subject.html", {"staffs": staffs, "courses": courses,
                                                     "subject": subject, "id": subject_id})


def edit_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(ID=course_id)
        s_id = request.POST.get("staffID")
        staff = CustomUser.objects.get(id=s_id)
        try:
            subject = Subject.objects.get(ID=subject_id)
            subject.subjectName = subject_name
            subject.courseID_id = course
            subject.staffID_id = staff

            subject.save()
            messages.success(request, "Subject Updated Successfully")
            return HttpResponseRedirect("/edit_subject/"+str(subject_id))
        except:
            messages.error(request, "Failed to Update Subject")
            return HttpResponseRedirect("/edit_subject/"+str(subject_id))
