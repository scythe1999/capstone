# Generated by Django 5.1.2 on 2024-10-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0038_tableofspecification_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableofspecification',
            name='group_id',
            field=models.IntegerField(),
        ),
    ]