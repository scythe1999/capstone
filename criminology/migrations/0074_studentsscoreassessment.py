# Generated by Django 5.1.3 on 2024-11-23 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0073_rename_studentsscore_studentsscoretos'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsScoreAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('studentid', models.IntegerField(blank=True, null=True, unique=True)),
                ('period', models.CharField(blank=True, max_length=200, null=True)),
                ('academic_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='criminology.academicyear')),
            ],
        ),
    ]
