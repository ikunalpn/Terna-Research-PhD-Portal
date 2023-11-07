from django.contrib import admin

from .models import (Student_Cards,User,StudentDetails,ProgressSeminarReport,StudentMasterList,StudentDocuments,Message,
                     Supervisor,Publication,ResearchGrant,ResearchExtraDetails,AdminDetails)

# Register your models here.
admin.site.register(Student_Cards)
admin.site.register(User)
admin.site.register(StudentDetails)
admin.site.register(ProgressSeminarReport)
admin.site.register(StudentMasterList)
admin.site.register(StudentDocuments)
admin.site.register(Message)
admin.site.register(Supervisor)
admin.site.register(Publication)
admin.site.register(ResearchGrant)
admin.site.register(ResearchExtraDetails)
admin.site.register(AdminDetails)
