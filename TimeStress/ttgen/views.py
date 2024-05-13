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
        form = EditRoom(request.POST, instance=room)
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
        form = EditInstructor(request.POST, instance=instructor)
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
        form = EditCourse(request.POST, instance=course)
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
        form = EditDepartment(request.POST, instance=department)
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
        form = EditSection(request.POST, instance=section)
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
    form = SectionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin_sections')
        else:
            print('invalid')
    context = {
        'form': form
        }
    return render(request, 'admin/add_section.html', context)

##########################################
# delete views
##########################################
@login_required
def admin_delete_room(request, room_id):
    room = Room.objects.filter(pk=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('admin_rooms')

@login_required
def admin_delete_instructor(request, instructor_id):
    instructor = Instructor.objects.filter(pk=instructor_id)
    if request.method == 'POST':
        instructor.delete()
        return redirect('admin_instructors')
    
@login_required
def admin_delete_course(request, course_id):
    course = Course.objects.filter(pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('admin_courses')

@login_required
def admin_delete_department(request, department_id):
    department = Department.objects.filter(pk=department_id)
    if request.method == 'POST':
        department.delete()
        return redirect('admin_departments')

@login_required
def admin_delete_section(request, section_id):
    section = Section.objects.filter(pk=section_id)
    if request.method == 'POST':
        section.delete()
        return redirect('admin_sections')
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
from django.http import HttpResponse
from django.shortcuts import render
import random

# Constants for demonstration
MAX_CLASSES_PER_DAY = 4
MAX_CONSECUTIVE_CLASSES = 2
MAX_CLASHES = 0

# Function to initialize a population of timetables
def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        timetable = generate_random_timetable()  # Generate a random timetable
        population.append(timetable)
    return population

# Function to generate a random timetable
def generate_random_timetable():
    # Logic to generate a random timetable for demonstration
    timetable = []
    for day in range(5):  # Assuming 5 working days
        daily_classes = random.randint(0, MAX_CLASSES_PER_DAY)
        timetable.append(daily_classes)
    return timetable

# Fitness function to evaluate the quality of a timetable
def fitness_function(timetable):
    # Calculate fitness score based on constraints
    fitness_score = 0
    for day_classes in timetable:
        if day_classes > MAX_CLASSES_PER_DAY:
            fitness_score -= 1
        if day_classes >= MAX_CONSECUTIVE_CLASSES:
            fitness_score -= 1
    return fitness_score

# Function to select fittest individuals from the population
def selection(population, fitness_scores):
    # Select individuals with higher fitness scores
    selected_population = []
    for i in range(len(population)):
        if fitness_scores[i] > 0:  # Considering positive fitness scores
            selected_population.append(population[i])
    return selected_population

# Function to create offspring through crossover
def crossover(selected_population):
    # Perform crossover (not implemented for demonstration)
    return selected_population

# Function to introduce random changes in the offspring
def mutation(offspring_population, mutation_rate):
    # Perform mutation (not implemented for demonstration)
    return offspring_population

# Function to check if the optimal solution is found
def optimal_solution_found(population):
    # Check if any timetable satisfies constraints (not implemented for demonstration)
    return False

# Function to select the best timetable from the final population
def select_best_timetable(population):
    # Select the timetable with the highest fitness score (not implemented for demonstration)
    return population[0]

# Function to validate if the generated timetable satisfies all constraints
def validate_timetable(timetable):
    # Check if timetable satisfies constraints (not implemented for demonstration)
    return True

# Function to save the timetable to the database or render it in a template
def save_timetable(timetable):
    # Save timetable to the database or render it in a template (not implemented for demonstration)
    pass

# Main function to generate timetable using genetic algorithm
def generate_timetable(request):
    # Initialize parameters
    population_size = 100
    mutation_rate = 0.1
    max_generations = 1000
    current_generation = 0

    # Initialize population
    population = initialize_population(population_size)

    while current_generation < max_generations:
        # Evaluate fitness of each timetable
        fitness_scores = [fitness_function(timetable) for timetable in population]

        # Select fittest individuals
        selected_population = selection(population, fitness_scores)

        # Create offspring through crossover
        offspring_population = crossover(selected_population)

        # Mutate offspring
        mutated_offspring = mutation(offspring_population, mutation_rate)

        # Replace old population with new generation
        population = mutated_offspring

        # Increment generation count
        current_generation += 1

        # Termination condition: Check if optimal timetable is found
        if optimal_solution_found(population):
            break

    # Select best timetable from final population
    best_timetable = select_best_timetable(population)

    # Validate timetable
    if validate_timetable(best_timetable):
        # Save timetable to database or render it in a template
        save_timetable(best_timetable)
        return HttpResponse("Timetable generated successfully.")
    else:
        return HttpResponse("Timetable generation failed due to constraints violation.")


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


