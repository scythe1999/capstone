# Generated by Django 5.1.3 on 2024-11-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0057_alter_answerkeytableofspecification_a_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerkey',
            name='a',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='assessment_exam_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='b',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='c',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='d',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]