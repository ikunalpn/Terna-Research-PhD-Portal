from django import forms
from .models import StudentDetails, StudentDocuments, Supervisor, Student_Cards


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['gender', 'dob', 'lives_in', 'contact_no', 'email']


class StudentDocumentForm(forms.ModelForm):
    class Meta:
        model = StudentDocuments
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_Cards
        fields = ['name', 'photo', 'status', 'scholar', 'title']

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ['name', 'email', 'contact_no', 'department', 'photo']

class DocumentSubmissionForm(forms.ModelForm):
    class Meta:
        model = StudentDocuments
        exclude = ['user']  #


class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)


class SupervisorProfileForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ['name', 'email', 'contact_no', 'department', 'photo']