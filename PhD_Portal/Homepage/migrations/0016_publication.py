# Generated by Django 4.2.3 on 2023-11-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0015_supervisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]
