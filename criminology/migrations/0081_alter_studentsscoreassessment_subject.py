# Generated by Django 5.1.3 on 2024-11-26 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0080_alter_studentsscoreassessment_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsscoreassessment',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='criminology.answerkeyassessment'),
        ),
    ]