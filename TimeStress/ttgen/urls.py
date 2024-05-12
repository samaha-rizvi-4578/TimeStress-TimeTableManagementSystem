from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.admindash, name='admindash'),
    # admin paths
    path('admins/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # view lists
    path('admins/rooms/', views.admin_rooms, name='admin_rooms'),
    path('admins/instructors/', views.admin_instructors, name='admin_instructors'),
    path('admins/courses/', views.admin_courses, name='admin_courses'),
    path('admins/departments/', views.admin_departments, name='admin_departments'),
    path('admins/sections/', views.admin_sections, name='admin_sections'),
    # add lists
    path('admins/add_room/', views.admin_add_room, name='admin_add_room'),
    path('admins/add_instructor/', views.admin_add_instructor, name='admin_add_instructor'),
    path('admins/add_course/', views.admin_add_course, name='admin_add_course'),
    path('admins/add_department/', views.admin_add_department, name='admin_add_department'),
    path('admins/add_section/', views.admin_add_section, name='admin_add_section'),
    # edit lists
    path('admins/edit_room/<int:room_id>/', views.admin_edit_room, name='admin_edit_room'),
    path('admins/edit_instructor/<int:instructor_id>/', views.admin_edit_instructor, name='admin_edit_instructor'),
    path('admins/edit_course/<str:course_id>/', views.admin_edit_course, name='admin_edit_course'),
    path('admins/edit_department/<int:department_id>/', views.admin_edit_department, name='admin_edit_department'),
    path('admins/edit_section/<int:section_id>/', views.admin_edit_section, name='admin_edit_section'),
    # delete lists
    path('admins/delete_room/<int:room_id>/', views.admin_delete_room, name='admin_delete_room'),
    path('admins/delete_instructor/<int:instructor_id>/', views.admin_delete_instructor, name='admin_delete_instructor'),
    path('admins/delete_course/<str:course_id>/', views.admin_delete_course, name='admin_delete_course'),
    path('admins/delete_department/<int:department_id>/', views.admin_delete_department, name='admin_delete_department'),
    path('admins/delete_section/<int:section_id>/', views.admin_delete_section, name='admin_delete_section'),
    
    # generate timetable
    path('admins/generate_timetable/', views.admin_generate_timetable, name='admin_generate_timetable'),
    #view timetable
    path('timetable/', views.user_timetable, name='timetable'),
    
]

