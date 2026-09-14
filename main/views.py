from django.shortcuts import render

from main.models import Experience, Education, Organization, Certificate


def show_main(request):
    context = {
        "name": "Qisthan Albani Fasyah",
        "npm": "2506621434",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Qisthan",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Qisthan",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

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