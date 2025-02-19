# Generated by Django 5.0.6 on 2024-06-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminology', '0020_remove_savedgeneratedquestions_subtopic_analyzing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedSubtopicTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('group_id', models.IntegerField(null=True)),
                ('subject', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=200)),
                ('subtopic', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=50)),
                ('mainquestion', models.CharField(max_length=600)),
                ('correct_answer', models.CharField(max_length=200)),
                ('distructor1', models.CharField(max_length=200)),
                ('distructor2', models.CharField(max_length=200)),
                ('distructor3', models.CharField(max_length=200)),
            ],
        ),
    ]
