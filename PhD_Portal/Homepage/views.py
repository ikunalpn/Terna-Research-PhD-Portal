from django.shortcuts import render, get_object_or_404

from .forms import PersonalDetailsForm, StudentDocumentForm, DocumentSubmissionForm, MessageForm, SupervisorProfileForm, \
    StudentForm, SupervisorForm
from .models import Student_Cards, User, ProgressSeminarReport, StudentMasterList, Message, Supervisor, Publication, \
    ResearchExtraDetails, AdminDetails
from .models import EventNotification, ResearchGrant
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Student_Cards, StudentDetails
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def student_detail(request, student_id):
    student = StudentDetails.objects.get(student_id=student_id)
    return render(request, 'homepage/student_detail.html', {'student': student})


# def login_page(request):
#     return render(request, 'homepage/login.html', {'error_message': ''})


def admin_home(request):
    admin = AdminDetails.objects.first()  # Assuming there's only one admin, you can adjust this as needed
    return render(request, 'admin/admin_home.html', {'admin': admin})

def home(request):
    students = Student_Cards.objects.all()  # Query the database to get a list of student objects
    completed_students = Student_Cards.objects.filter(status="Completed").count()

    # Count the number of students with "Ongoing" status
    ongoing_students = Student_Cards.objects.filter(status="Ongoing").count()

    context = {
        'students': students,
        'completed_students': completed_students,
        'ongoing_students': ongoing_students,
    }
    return render(request, 'Homepage/home.html',context)


def news(request):
    return render(request, 'Homepage/news.html')


def about(request):
    return render(request, 'Homepage/about.html')


def event(request):
    return render(request, 'Homepage/event.html')


def scholars(request):
    return render(request, 'Homepage/scholar.html')


def gallery(request):
    return render(request, 'Homepage/gallery.html')


def student_card(request):
    students = Student_Cards.objects.all()
    return render(request, 'homepage/scholar.html', {'students': students})


def phd_status(request, status=None):
    if status is None or status == 'all':
        students = Student_Cards.objects.all()
    else:
        students = Student_Cards.objects.filter(status=status)

    student_data = [{'name': student.name, 'status': student.status} for student in students]

    return JsonResponse({'students': student_data})


def admin_dashboard(request):
    return render(request, 'Admin/admin_home.html', {'user': request.user})


def progress_seminar_report(request):
    records = ProgressSeminarReport.objects.all()
    return render(request,'Admin/progress_seminar_report.html', {'records': records})


def master_list(request):
    student_details = StudentDetails.objects.all()
    student_master_list = StudentMasterList.objects.all()

    return render(request, 'Admin/master_list.html', {
        'student_details': student_details,
        'student_master_list': student_master_list,
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            print(f"User found: {user.username}, Role: {user.role}")  # Add this line for debugging

            if user.role == 'student':
                try:
                    if user.username == 'john':
                        student = StudentDetails.objects.get(student_id=1)
                        return render(request, 'student/student_home.html', {'student': student})
                    elif user.username == 'dave':
                        student = StudentDetails.objects.get(student_id=2)
                        return render(request, 'student/student_home.html', {'student': student})
                    elif user.username == 'ram':
                        student = StudentDetails.objects.get(student_id=3)
                        return render(request, 'student/student_home.html', {'student': student})
                    elif user.username == 'ammy':
                        student = StudentDetails.objects.get(student_id=4)
                        return render(request, 'student/student_home.html', {'student': student})
                    return render(request, 'student/student_home.html')
                except StudentDetails.DoesNotExist:
                    # Handle the case where the user doesn't have associated student details
                    return render(request, 'student/student_home.html', {'error_message': 'Student details not found'})
            elif user.role == 'admin':
                print("Admin logged in")  # Add this line for debugging
                return render(request, 'admin/admin_home.html')
            elif user.role == 'supervisor':
                if user.username == 'bhide':
                    try:
                        # Fetch the supervisor with the name "A.B.Bhide"
                        supervisor = Supervisor.objects.get(name='A.B.Bhide')
                        print(supervisor)
                        return render(request, 'supervisor/supervisor_home.html', {'supervisor': supervisor})
                    except Supervisor.DoesNotExist:
                        return HttpResponse("Supervisor not found.")
                return render(request, 'Supervisor/supervisor_home.html')
        except User.DoesNotExist:
            print("User not found")  # Add this line for debugging
            return render(request, 'homepage/login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'homepage/login.html')


def edit_personal_details(request):
    student = StudentDetails.objects.get(id=1)

    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'student/student_home.html', {'student': student})  # Redirect to the student home page after editing
    else:
        form = PersonalDetailsForm(instance=student)

    return render(request, 'student/regform.html', {'form': form, 'student':student})


def submit_documents(request):
    if request.method == 'POST':
        student = StudentDetails.objects.get(id=1)
        form = StudentDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new StudentDocuments instance and associate it with the current user
            student_documents = form.save(commit=False)
            student_documents.user = request.user  # Assuming you're using the built-in User model
            student_documents.save()
            return render(request, 'student/student_home.html', {'student': student}) # Redirect to the student home page after submission
    else:
        form = StudentDocumentForm()

    return render(request, 'student/student_document.html', {'form': form})


def document_submission(request):
    if request.method == 'POST':
        student = StudentDetails.objects.get(id=1)
        form = DocumentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the documents with the current user
            student_document = form.save(commit=False)
            student_document.user = request.user  # Assuming you're using the built-in User model
            student_document.save()
            return render(request, 'student/student_home.html', {'student': student})   # Redirect to the student home page after submission
    else:
        form = DocumentSubmissionForm()

    return render(request, 'student/student_document.html', {'form': form})


def reg_sym(request):
    return render(request, 'student/Reg_symposium.html')


def student_notice(request):
    return render(request, 'student/notice.html')


def forum(request):
    return render(request, 'student/forum.html')

def edit_profile(request):
    supervisor = Supervisor.objects.get(name="A.B.Bhide")
    if request.method == 'POST':
        form = SupervisorProfileForm(request.POST, request.FILES, instance=supervisor)
        if form.is_valid():
            form.save()
            supervisor = Supervisor.objects.get(name='A.B.Bhide')
            return render(request, 'supervisor/supervisor_home.html', {'supervisor': supervisor})
    else:
        form = SupervisorProfileForm(instance=supervisor)

    return render(request, 'supervisor/edit_profile.html', {'form': form})

def supervisior_student_details(request):
    students = Student_Cards.objects.all()
    return render(request, 'supervisor/supervisor_student_detail.html', {'students': students})


def supervisor_remuneration(request):
    supervisors = Supervisor.objects.all()
    return render(request, 'supervisor/supervisor_remuneration.html', {'supervisors': supervisors})


def publication_details(request):
    publications = Publication.objects.all()
    return render(request, 'supervisor/publication_details.html', {'publications': publications})


def event_notifications(request):
    notifications = EventNotification.objects.all()
    return render(request, 'supervisor/event_notifications.html', {'notifications': notifications})


def research_grant_detail(request):
    publications = Publication.objects.all()
    # return render(request, 'supervisor/research_grant_detail.html', {'grant': ResearchGrant.objects.all()})



def supervisor_notice(request):
    return render(request, 'supervisor/notice.html')


def research_grant_details(request):
    # Query the ResearchExtraDetails model to retrieve all rows
    grants = ResearchExtraDetails.objects.all()

    context = {
        'grants': grants
    }

    return render(request, 'supervisor/research_grant_detail.html', context)


def super_forum(request):
    return render(request, 'supervisor/Forum.html')


def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('/admin_home/')
            # return render(request, 'admin/admin_home.html')
            # return render(request, 'admin/admin_home.html')

    else:
        student_form = StudentForm()

    return render(request, 'admin/add_student.html', {'form': student_form})

def add_supervisor(request):
    if request.method == 'POST':
        supervisor_form = SupervisorForm(request.POST, request.FILES)
        if supervisor_form.is_valid():
            supervisor_form.save()
            messages.success(request, 'Supervisor added successfully.')
            return render(request, 'admin/admin_home.html')

    else:
        supervisor_form = SupervisorForm()

    return render(request, 'admin/add_supervisor.html', {'form': supervisor_form})