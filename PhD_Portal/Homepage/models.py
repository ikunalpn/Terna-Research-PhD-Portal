from django.db import models

# Create your models here.





class Student_Cards(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student_photos/')
    status = models.CharField(max_length=100)
    scholar = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StudentDetails(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    REGISTER_CHOICES = (
        ('Residential', 'Residential'),
        ('Non-Residential', 'Non-Residential'),
    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.OneToOneField(Student_Cards, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)
    year = models.IntegerField()

    research_title = models.CharField(max_length=200)
    area_of_research = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    guide = models.CharField(max_length=100)
    co_guide = models.CharField(max_length=100,default='NA')
    register_as = models.CharField(max_length=20, choices=REGISTER_CHOICES)
    register_on = models.DateField()

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()

    lives_in = models.CharField(max_length=100)
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.student.name


class ProgressSeminarReport(models.Model):
    student = models.OneToOneField('Student_Cards', on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    supervisor_name = models.CharField(max_length=100)
    topic_approval_seminar = models.CharField(max_length=20)
    sps_01 = models.CharField(max_length=20)
    aps_01 = models.CharField(max_length=20)
    sps_02 = models.CharField(max_length=20)
    aps_02 = models.CharField(max_length=20)
    sps_03 = models.CharField(max_length=20)
    aps_03 = models.CharField(max_length=20)

    def __str__(self):
        return self.student.name


class StudentMasterList(models.Model):
    CATEGORY_CHOICES = (
        ('OPEN', 'OPEN'),
        ('ST', 'ST'),
        ('SC', 'SC'),
        ('OBC', 'OBC'),
        ('NT', 'NT'),
    )

    student = models.ForeignKey(Student_Cards, on_delete=models.CASCADE, null=True)
    # Additional attributes specific to StudentMasterList
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    enrollment_number = models.CharField(max_length=100)
    external_evaluator = models.CharField(max_length=100, default='NA')
    internal_evaluator = models.CharField(max_length=100, default='NA')
    chairman = models.CharField(max_length=100,default='NA')
    pre_synopsis_date = models.DateField()
    synopsis_date = models.DateField()
    thesis_date = models.DateField()
    defence_date = models.DateField()

    def __str__(self):
        return self.student.name



class User(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('supervisor', 'Supervisor'),
    )
    # student = models.OneToOneField(Student_Cards, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class StudentDocuments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_letter = models.FileField(upload_to='documents/')
    selection_letter = models.FileField(upload_to='documents/')
    guide_approval_letter = models.FileField(upload_to='documents/')
    course_work_certificate = models.FileField(upload_to='documents/')
    topic_approval_permission = models.FileField(upload_to='documents/')
    rac_report = models.FileField(upload_to='documents/')
    dept_approval_letter = models.FileField(upload_to='documents/')
    uni_topic_approval_form = models.FileField(upload_to='documents/')
    topic_approval = models.FileField(upload_to='documents/')
    topic_reg_form = models.FileField(upload_to='documents/')
    marksheets = models.FileField(upload_to='documents/', blank=True, null=True)
    registration_letter = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"Documents for {self.user.username}"


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Supervisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='supervisor_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class EventNotification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()


class ResearchGrant(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    grant_amount = models.DecimalField(max_digits=10, decimal_places=2)
    grant_provider = models.CharField(max_length=100)
    grant_deadline = models.DateField()

    def __str__(self):
        return self.title

class ResearchExtraDetails(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    grant_amount = models.DecimalField(max_digits=10, decimal_places=2)
    grant_provider = models.CharField(max_length=100)
    grant_deadline = models.DateField()

    def __str__(self):
        return self.title

class AdminDetails(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='admin_photos/')
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name