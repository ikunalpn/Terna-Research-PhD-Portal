# Generated by Django 4.2.3 on 2023-11-03 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0007_remove_studentmasterlist_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmasterlist',
            name='email',
        ),
    ]
