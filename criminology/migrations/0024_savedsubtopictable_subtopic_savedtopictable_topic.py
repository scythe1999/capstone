# Generated by Django 5.0.6 on 2024-06-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0023_savedtopictable'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedsubtopictable',
            name='subtopic',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='savedtopictable',
            name='topic',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
