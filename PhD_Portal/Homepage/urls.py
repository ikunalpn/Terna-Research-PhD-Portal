from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views  # Import the views module from your app
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('scholars/', views.student_card, name='scholars'),
    path('scholars/', views.phd_status, name='phd_status'),
    path('phd_status/', views.phd_status, name='phd_status'),
    path('login/', views.login_view, name='login_view'),
    # path('student_view/', views.student_view, name='student_view'),
    # path('login/', views.login_page, name='login'),
    # path('student/', views.student_view, name='student_view'),
    # path('admin/', views.admin_view, name='admin_view'),
    path('news/', views.news, name='news'),
    path('about/',views.about,name='about'),
    path('event/', views.event, name='event'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('logout/', views.login_view, name='logout'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('progress_seminar_report/', views.progress_seminar_report, name='progress_seminar_report'),
    path('master_list/', views.master_list, name='master_list'),
    path('regform/', views.edit_personal_details, name='regform'),
    path('regform/<int:student_id>/', views.edit_personal_details, name='edit_personal_details'),
    path('upload_docs/', views.submit_documents, name='upload_docs'),
    path('reg_sym/', views.reg_sym, name='reg_sym'),
    path('student_notice/', views.student_notice, name='student_notice'),
    path('supervisor_notice/', views.supervisor_notice, name='supervisor_notice'),
    # path('conversation/<int:recipient_id>/', views.conversation, name='conversation'),
    # path('conversation/', views.conversation, name='conversation'),
    path('forum/', views.forum, name='forum'),
    path('super_forum/', views.super_forum, name='super_forum'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('supervisor_student-details/', views.supervisior_student_details, name='supervisor_student-details'),
    # path('admin_home/', views., name='admin_home'),
    path('remuneration/', views.supervisor_remuneration, name='supervisor_remuneration'),
    path('publication/', views.publication_details, name='publication_details'),
    path('event-notifications/', views.event_notifications, name='event_notifications'),
    path('research_grants/', views.research_grant_detail, name='research_grant_detail'),
    path('research_grant_details/', views.research_grant_details, name='research_grant_details'),

    path('add_student/', views.add_student, name='add_student'),
    path('add_supervisor/', views.add_supervisor, name='add_supervisor'),

    # This maps the root URL to the home view
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
