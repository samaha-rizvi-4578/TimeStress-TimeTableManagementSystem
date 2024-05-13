from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=6, primary_key=True)
    seating_capacity = models.IntegerField(default=50)

    def __str__(self):
        return self.room_number

class Instructor(models.Model):
    id_number = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.id_number} - {self.name}'

class Course(models.Model):
    course_number = models.CharField(max_length=5, primary_key=True)
    course_name = models.CharField(max_length=100)
    max_students = models.IntegerField(default=50)
    classes_per_week = models.IntegerField(default=3)
    class_duration = models.IntegerField(default=1)
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return f'{self.course_number} - {self.course_name}'

class Department(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Section(models.Model):
    section_id = models.CharField(max_length=25, primary_key=True)
    batch_number = models.IntegerField(default=21)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.section_id
