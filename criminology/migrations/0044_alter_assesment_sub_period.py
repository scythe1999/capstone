# Generated by Django 5.1.2 on 2024-11-09 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0043_assesment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assesment',
            name='sub_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='criminology.subject'),
        ),
    ]