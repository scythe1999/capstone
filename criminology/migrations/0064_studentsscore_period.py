# Generated by Django 5.1.3 on 2024-11-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0063_studentsscore_firstname_studentsscore_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsscore',
            name='period',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
