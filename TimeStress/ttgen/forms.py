from django import forms
from django.forms import ModelForm
from .models import Room, Instructor, Course, Department, Section
from django.utils.translation import gettext_lazy as _

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label=_('Upload CSV'))

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'seating_capacity']
        labels = {
            "room_number": _("Room ID"),
            "seating_capacity": _("Capacity")
        }

class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['id_number', 'name', 'cnic']
        labels = {
            "id_number": _("Teacher UID"),
            "name": _("Full Name"),
            "cnic": _("CNIC")
        }

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'max_students', 'instructors', 'classes_per_week', 'class_duration']
        labels = {
            "course_number": _("Course ID"),
            "course_name": _("Course Name"),
            "max_students": _("Course Capacity"),
            "instructors": _("Course Teachers"),
            "classes_per_week": _("Classes Per Week"),
            "class_duration": _("Class Duration")
        }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'courses']
        labels = {
            "name": _("Department Name"),
            "courses": _("Corresponding Courses")
        }

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'batch_number', 'department', 'course', 'room', 'instructor']
        labels = {
            "section_id": _("Section ID"),
            "batch_number": _("Batch Number"),
            "department": _("Department"),
            "course": _("Course"),
            "room": _("Room"),
            "instructor": _("Instructor")
        }

class EditSection(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

class EditCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
class EditDepartment(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
class EditInstructor(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

class EditRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            
