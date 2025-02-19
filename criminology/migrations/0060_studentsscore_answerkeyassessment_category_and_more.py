# Generated by Django 5.1.3 on 2024-11-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0059_rename_answerkey_answerkeyassessment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='answerkeyassessment',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='answerkeytableofspecification',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
