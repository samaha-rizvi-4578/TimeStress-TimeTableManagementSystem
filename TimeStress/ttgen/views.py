from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from accounts.models import Profile  # Import the Profile model
import csv

# Views

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def terms(request):
    return render(request, 'terms.html', {})

#redireccting

@login_required
def admindash(request):
    # Logic for admin dashboard
    if request.user.profile.user_type == 'admin':
        return admin_dashboard(request)
    else:
        return user_timetable(request)
        
#admin views
@login_required
def admin_dashboard(request):
    # Logic for admin dashboard
    if request.user.profile.user_type == 'admin':
        return render(request, 'admin/dashboard.html')
    else:
        return redirect('admindash')
############################################################
# view lists
############################################################
@login_required
def admin_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'admin/rooms.html', {'rooms': rooms})


def admin_instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'admin/instructors.html', {'instructors': instructors})

@login_required
def admin_courses(request):
    courses = Course.objects.all()
    return render(request, 'admin/courses.html', {'courses': courses})

@login_required
def admin_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin/departments.html', {'departments': departments})

@login_required
def admin_sections(request):
    sections = Section.objects.all()
    return render(request, 'admin/sections.html', {'sections': sections})

######################################
#edit views
######################################


@login_required
def admin_edit_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('admin_rooms')
    else:
        form = RoomForm(instance=room)
    return render(request, 'admin/edit_room.html', {'form': form})

@login_required
def admin_edit_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('admin_instructors')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'admin/edit_instructor.html', {'form': form})

@login_required
def admin_edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('admin_courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'admin/edit_course.html', {'form': form})

@login_required
def admin_edit_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('admin_departments')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'admin/edit_department.html', {'form': form})

@login_required
def admin_edit_section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('admin_sections')
    else:
        form = EditForm(instance=section)
    return render(request, 'admin/edit_section.html', {'form': form})

###############################################
# add views
###############################################
@login_required
def admin_add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_rooms')
    else:
        form = RoomForm()
    return render(request, 'admin/add_room.html', {'form': form})

@login_required
def admin_add_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_instructors')
    else:
        form = InstructorForm()
    return render(request, 'admin/add_instructor.html', {'form': form})

@login_required
def admin_add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_courses')
    else:
        form = CourseForm()
    return render(request, 'admin/add_course.html', {'form': form})

@login_required
def admin_add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_departments')
    else:
        form = DepartmentForm()
    return render(request, 'admin/add_department.html', {'form': form})

@login_required
def admin_add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_sections')
    else:
        form = SectionForm()
    return render(request, 'admin/add_section.html', {'form': form})

##########################################
# delete views
##########################################
@login_required
def admin_delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            room.delete()
            return redirect('admin_rooms')
    else:
        form = DeleteForm()
    return render(request, 'admin/delete_room.html', {'form': form, 'room': room})

@login_required
def admin_delete_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            instructor.delete()
            return redirect('admin_instructors')
    else:
        form = DeleteForm()
    return render(request, 'admin/delete_instructor.html', {'form': form, 'instructor': instructor})

@login_required
def admin_delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            course.delete()
            return redirect('admin_courses')
    else:
        form = DeleteForm()
    return render(request, 'admin/delete_course.html', {'form': form, 'course': course})

@login_required
def admin_delete_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            department.delete()
            return redirect('admin_departments')
    else:
        form = DeleteForm()
    return render(request, 'admin/delete_department.html', {'form': form, 'department': department})

@login_required
def admin_delete_section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            section.delete()
            return redirect('admin_sections')
    else:
        form = DeleteForm()
    return render(request, 'admin/delete_section.html', {'form': form, 'section': section})
########################################
# generate timetable
########################################
@login_required
def admin_generate_timetable(request):
    generate_timetable(request)
    # Logic for generating timetable using genetic algorithm and constraints
    return render(request, 'admin/generate_timetable.html')

########################################
#generate timetable fucntion
########################################
def generate_timetable(request):
    # Logic for generating timetable using genetic algorithm and constraints
    return HttpResponse("Timetable generated successfully.")

# User Views

@login_required
def user_timetable(request):
    # Logic for displaying user's timetable
    return render(request, 'timetable.html')

# Timetable Generation Views

@login_required
def generate_timetable(request):
    # Logic for generating timetable using genetic algorithm and constraints
    return HttpResponse("Timetable generated successfully.")

@login_required
def download_timetable(request):
    # Logic for downloading timetable as PDF or Excel
    return HttpResponse("Timetable downloaded successfully.")


