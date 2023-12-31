# Generated by Django 4.2.3 on 2023-11-03 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0005_progressseminarreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMasterList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('OPEN', 'OPEN'), ('ST', 'ST'), ('SC', 'SC'), ('OBC', 'OBC'), ('NT', 'NT')], max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=15)),
                ('enrollment_number', models.CharField(max_length=100)),
                ('academic_year', models.CharField(max_length=100)),
                ('supervisor_name', models.CharField(max_length=100)),
                ('external_evaluator', models.CharField(max_length=100)),
                ('internal_evaluator', models.CharField(max_length=100)),
                ('chairman', models.CharField(max_length=100)),
                ('title_of_thesis', models.CharField(max_length=200)),
                ('coursework_completed', models.BooleanField(default=False)),
                ('topic_approval_seminar', models.CharField(max_length=20)),
                ('sps_01', models.CharField(max_length=20)),
                ('aps_01', models.CharField(max_length=20)),
                ('sps_02', models.CharField(max_length=20)),
                ('aps_02', models.CharField(max_length=20)),
                ('sps_03', models.CharField(max_length=20)),
                ('aps_03', models.CharField(max_length=20)),
                ('sps_04', models.CharField(max_length=20)),
                ('aps_04', models.CharField(max_length=20)),
                ('sps_05', models.CharField(max_length=20)),
                ('aps_05', models.CharField(max_length=20)),
                ('sps_06', models.CharField(max_length=20)),
                ('aps_06', models.CharField(max_length=20)),
                ('pre_synopsis_date', models.DateField()),
                ('synopsis_date', models.DateField()),
                ('thesis_date', models.DateField()),
                ('defence_date', models.DateField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Homepage.student_cards')),
            ],
        ),
    ]
