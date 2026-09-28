from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),

    path("education/add/", create_education, name="create_education"),
    path("education/", show_education, name="show_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),

    path("organization/", show_organization, name="show_organization"),
    path("certificate/", show_certificate, name="show_certificate"),

    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/edit/",update_project,name="update_project"),

    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    # Tambahkan path ini ke dalam urlpatterns
    path("projects/<uuid:project_id>/star/",toggle_star,name="toggle_star",),
]