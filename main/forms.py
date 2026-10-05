from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school",
            "level",
            "year",
            "image_url",
            "gmaps_url",
        ]

        labels = {
            "school": "Nama Sekolah",
            "level": "Jenjang sekolah",
            "year": "Tahun berserkolah",
            "image_url": "URL Foto Sekolah",
            "gmaps_url": "URL GMaps Sekolah",
        }

        widgets = {
            "school": TextInput(
                attrs={
                    "placeholder": "Tuliskan nama Sekolah",
                    "maxlength": 255,
                }
            ),
            "level": TextInput(
                attrs={
                    "placeholder": "Jenjang kamu bersekolah",
                    "maxlength": 100,
                }
            ),
            "year": TextInput(
                attrs={
                    "placeholder": "Tahun kamu berserkolah",
                    "maxlength": 50,
                }
            ),
            "image_url": URLInput(
                attrs={
                    "placeholder": "Link Foto Sekolah",
                }
            ),
            "gmaps_url": URLInput(
                attrs={
                    "placeholder": "Link GMaps",
                }
            ),
        }

    def clean_school(self):
        school = strip_tags(self.cleaned_data["school"]).strip()

        if not school:
            raise ValidationError(
                "Nama sekolah tidak boleh hanya berisi tag HTML."
            )

        return school

    def clean_level(self):
        return strip_tags(self.cleaned_data["level"]).strip()

    def clean_year(self):
        return strip_tags(self.cleaned_data["year"]).strip()

# class OrganizationForm(ModelForm):
#     class Meta:
#         model = Organization
#         fields = [
#                 "name",
#                 "position",
#                 "year",
#                 "image_logo_url",
#         ]
        
#         labels = {
#                 "name": "Nama Organisasi",
#                 "position": "Jabatan",
#                 "year": "Tahun menjabat",
#                 "image_logo_url": "Logo Organisasi",
#         }
        
#         widgets = {
#                     "name": TextInput(
#                         attrs={
#                             "placeholder": "Tuliskan nama Organisasi",
#                             "maxlength": 255,
#                         }
#                     ),
#                     "position": TextInput(
#                         attrs={
#                             "placeholder": "Posisi di Organisasi",
#                             "maxlength": 255,
#                         }
#                     ),
#                     "year": TextInput(
#                         attrs={
#                             "placeholder": "Lama menjabat",
#                             "maxlength": 50,
#                         }
#                     ),
#                     "image_logo_url": URLInput(
#                         attrs={
#                             "placeholder": "Link logo organisasi",
#                         }
#                     ),
#         }