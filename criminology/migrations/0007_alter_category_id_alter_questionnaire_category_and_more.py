# Generated by Django 5.0.6 on 2024-05-28 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0006_alter_questionnaire_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='criminology.category'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='criminology.subject'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='subtopic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='criminology.subtopic'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='criminology.topic'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
