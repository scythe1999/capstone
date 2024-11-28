# Generated by Django 5.1.2 on 2024-11-09 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0042_subject_subject_pw'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_period', models.CharField(max_length=200)),
                ('period', models.CharField(max_length=200)),
                ('academic_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='criminology.academicyear')),
            ],
        ),
    ]