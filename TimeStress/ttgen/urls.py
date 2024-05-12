from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('admin_dashboard/', views.admindash, name='admindash'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/rooms/', views.admin_rooms, name='admin_rooms'),
    path('admin/instructors/', views.admin_instructors, name='admin_instructors'),
    path('admin/courses/', views.admin_courses, name='admin_courses'),
    path('admin/departments/', views.admin_departments, name='admin_departments'),
    path('admin/sections/', views.admin_sections, name='admin_sections'),
    path('admin/generate_timetable/', views.admin_generate_timetable, name='admin_generate_timetable'),
    path('admin/edit_section/<int:section_id>/', views.admin_edit_section, name='admin_edit_section'),
    path('timetable/', views.user_timetable, name='timetable'),
    
]

