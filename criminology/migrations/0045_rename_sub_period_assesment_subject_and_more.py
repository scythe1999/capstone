# Generated by Django 5.1.2 on 2024-11-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0044_alter_assesment_sub_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assesment',
            old_name='sub_period',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='assesment',
            name='assesment_number',
            field=models.IntegerField(default=0),
        ),
    ]
