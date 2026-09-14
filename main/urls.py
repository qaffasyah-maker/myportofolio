from django.urls import path

from main.views import show_main, show_experience, show_education, show_organization, show_certificate

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("organization/", show_organization, name="show_organization"),
    path("certificate/", show_certificate, name="show_certificate"),
]