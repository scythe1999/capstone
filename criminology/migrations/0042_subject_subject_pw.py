# Generated by Django 5.1.2 on 2024-11-08 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0041_delete_savedgeneratedquestions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_pw',
            field=models.IntegerField(default=0),
        ),
    ]
