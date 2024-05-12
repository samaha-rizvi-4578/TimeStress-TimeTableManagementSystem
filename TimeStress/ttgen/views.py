from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
import random as rnd


# Views

def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def terms(request):
    return render(request, 'terms.html', {})
# Admin Views

def admin_dashboard(request):
    # Logic for admin dashboard
    return render(request, 'admin/dashboard.html')

def admin_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'admin/rooms.html', {'rooms': rooms})

def admin_instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'admin/instructors.html', {'instructors': instructors})

def admin_courses(request):
    courses = Course.objects.all()
    return render(request, 'admin/courses.html', {'courses': courses})

def admin_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin/departments.html', {'departments': departments})

def admin_sections(request):
    sections = Section.objects.all()
    return render(request, 'admin/sections.html', {'sections': sections})

def admin_generate_timetable(request):
    # Logic for generating timetable using genetic algorithm and constraints
    return HttpResponse("Timetable generated successfully.")

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

# User Views

def user_timetable(request):
    # Logic for displaying user's timetable
    return render(request, 'timetable.html')

# Timetable Generation Views

def generate_timetable(request):
    # Logic for generating timetable using genetic algorithm and constraints
    return HttpResponse("Timetable generated successfully.")

def download_timetable(request):
    # Logic for downloading timetable as PDF or Excel
    return HttpResponse("Timetable downloaded successfully.")

from accounts.models import Profile  # Import the Profile model

def admindash(request):
    # Retrieve the logged-in user's profile
    profile = Profile.objects.get(user=request.user)
    
    # Check if the user type is 'admin' and render the corresponding template
    if profile.user_type == 'admin':
        return render(request, 'admin/dashboard.html')
    else:
        return render(request, 'timetable.html')

# Add more views for uploading CSV, editing/deleting model instances, etc.
