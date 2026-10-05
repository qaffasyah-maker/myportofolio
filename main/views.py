from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import datetime
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied       
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from main.models import *
from main.forms import *

def is_editor(user):
    return user.groups.filter(name="Editor").exists()

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'belum ada sesi login')
    context = {
        "name": "Qisthan Albani Fasyah",
        "npm": "2506621434",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Qisthan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "daftar Sekolah berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Qisthan",
        "form": form,
    }
    return render(request, "education_form.html", context)

def show_education(request):
    context = {
        "name": "Qisthan",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def get_education_json(request):
    school_query = request.GET.get("school", "").strip()
    education_list = Education.objects.prefetch_related("starred_by").all()

    if school_query:
        education_list = education_list.filter(
            school__icontains=school_query
        )

    data = []

    for education in education_list:
        starred_users = education.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        data.append({
            "pk": str(education.id),
            "fields": {
                "school": education.school,
                "level": education.level,
                "year": education.year,
                "image_url": education.image_url,
                "gmaps_url": education.gmaps_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
            }
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_education_ajax(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return JsonResponse(
            {
                "message": "Hanya pemilik portofolio yang dapat menambahkan pendidikan."
            },
            status=403,
        )

    form = EducationForm(request.POST)

    if form.is_valid():
        education = form.save()

        return JsonResponse(
            {
                "message": "Pendidikan berhasil ditambahkan.",
                "pk": str(education.id),
            },
            status=201,
        )

    return JsonResponse(
        {
            "errors": form.errors.get_json_data(),
        },
        status=400,
    )

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Daftar Sekolah berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def show_organization(request):
    context = {
        "name": "Qisthan",
        "organization_list": Organization.objects.all(),
    }
    return render(request, "organization.html", context)

def show_certificate(request):
    context = {
        "name": "Qisthan",
        "certificate_list": Certificate.objects.all(),
    }
    return render(request, "certificate.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Qisthan",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def update_project(request, project_id):
    if not request.user.is_superuser and not is_editor(request.user):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Qisthan",
        "form": form,
    }

    return render(request, "projects_form.html", context)


def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Burhan",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
