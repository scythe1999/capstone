# Generated by Django 5.1.3 on 2024-11-26 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0086_studentsscoreassessment_studentid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsscoreassessment',
            name='stud',
        ),
        migrations.RemoveField(
            model_name='studentsscoretos',
            name='stud',
        ),
    ]
