# Generated by Django 4.2.3 on 2023-11-05 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0012_remove_studentmasterlist_aps_04_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('supervisor', 'Supervisor')], max_length=20),
        ),
        migrations.CreateModel(
            name='StudentDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_letter', models.FileField(upload_to='documents/')),
                ('selection_letter', models.FileField(upload_to='documents/')),
                ('guide_approval_letter', models.FileField(upload_to='documents/')),
                ('course_work_certificate', models.FileField(upload_to='documents/')),
                ('topic_approval_permission', models.FileField(upload_to='documents/')),
                ('rac_report', models.FileField(upload_to='documents/')),
                ('dept_approval_letter', models.FileField(upload_to='documents/')),
                ('uni_topic_approval_form', models.FileField(upload_to='documents/')),
                ('topic_approval', models.FileField(upload_to='documents/')),
                ('topic_reg_form', models.FileField(upload_to='documents/')),
                ('marksheets', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('registration_letter', models.FileField(upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.user')),
            ],
        ),
    ]
