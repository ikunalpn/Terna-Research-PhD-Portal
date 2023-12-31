# Generated by Django 4.2.3 on 2023-11-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0019_researchextradetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='admin_photos/')),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]
