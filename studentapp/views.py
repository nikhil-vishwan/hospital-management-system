
from django.shortcuts import render
from .models import Admin, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, Notificationstaff



def signup(request):
    return render(request, 'signup.html ')


def index(request):
    # Retrieve data from your models (replace with your actual model names)
    admins = Admin.objects.all()
    staffs = Staffs.objects.all()
    courses = Courses.objects.all()
    subjects = Subjects.objects.all()
    students = Students.objects.all()
    attendance = Attendance.objects.all()
    attendancereport = AttendanceReport.objects.all()
    leavereportstudent = LeaveReportStudent.objects.all()
    leavereportstaff = LeaveReportStaff.objects.all()
    feedbackstudent = FeedBackStudent.objects.all()
    feedbackstaffs = FeedBackStaffs.objects.all()
    notificationstudent = NotificationStudent.objects.all()
    notificationstaff = Notificationstaff.objects.all()

    # Render the HTML template with the retrieved data
    return render(request, 'studapp/index.html', {
        'admins': admins,
        'staffs': staffs,
        'courses': courses,
        'subjects': subjects,
        'students': students,
        'attendance': attendance,
        'attendancereport': attendancereport,
        'leavereportstudent': leavereportstudent,
        'leavereportstaff': leavereportstaff,
        'feedbackstudent': feedbackstudent,
        'feedbackstaffs': feedbackstaffs,
        'notificationstudent': notificationstudent,
        'notificationstaff': notificationstaff,
    })

def student_dashboard(request):
    # Retrieve student information based on the logged-in user (you need to implement this logic)
    student = Students.objects.get(email=request.user.email)

    # Retrieve related data (adjust relationships according to your models)
    courses = Courses.objects.filter(students=student)
    attendance = AttendanceReport.objects.filter(student_id=student)
    leave_reports = LeaveReportStudent.objects.filter(student_id=student)
    feedbacks = FeedBackStudent.objects.filter(student_id=student)
    notifications = NotificationStudent.objects.filter(student_id=student)

    return render(request, 'studapp/student.html', {
        'student': student,
        'courses': courses,
        'attendance': attendance,
        'leave_reports': leave_reports,
        'feedbacks': feedbacks,
        'notifications': notifications,
    })

