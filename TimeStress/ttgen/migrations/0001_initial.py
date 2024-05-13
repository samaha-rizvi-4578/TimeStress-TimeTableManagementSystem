# Generated by Django 5.0.4 on 2024-05-13 00:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_number', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('max_students', models.IntegerField(default=50)),
                ('classes_per_week', models.IntegerField(default=3)),
                ('class_duration', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id_number', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cnic', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('seating_capacity', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('courses', models.ManyToManyField(to='ttgen.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='ttgen.instructor'),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('batch_number', models.IntegerField(default=21)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttgen.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttgen.department')),
            ],
        ),
    ]
