from django.test import TestCase
from django.urls import reverse

from main.models import Education, Organization, Certificate


class MainTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            school="SDIT AL HARAKI",
            level="SD",
            year="2013 - 2019",
        )

        self.organization = Organization.objects.create(
            name="FUKI Fasilkom UI",
            position="Wakil Ketua Biro / Biro Creative Media",
            year="2026 - Sekarang",
        )

        self.certificate = Certificate.objects.create(
            name="Hak Cipta Film",
            issuer="Kementerian Hukum Republik Indonesia",
            year="2026",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(
            response,
            f'href="{reverse("main:show_education")}"'
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_education_model(self):
        self.assertEqual(str(self.education), "SDIT AL HARAKI")
        self.assertEqual(self.education.level, "SD")
        self.assertEqual(self.education.year, "2013 - 2019")

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.school)
        self.assertContains(response, self.education.level)
        self.assertContains(response, self.education.year)
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_organization_model(self):
        self.assertEqual(str(self.organization), "FUKI Fasilkom UI")
        self.assertEqual(
            self.organization.position,
            "Wakil Ketua Biro / Biro Creative Media"
        )
        self.assertEqual(self.organization.year, "2026 - Sekarang")

    def test_organization_page(self):
        response = self.client.get(reverse("main:show_organization"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "organization.html")
        self.assertContains(response, self.organization.name)
        self.assertContains(response, self.organization.position)
        self.assertContains(response, self.organization.year)
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_certificate_model(self):
        self.assertEqual(str(self.certificate), "Hak Cipta Film")
        self.assertEqual(
            self.certificate.issuer,
            "Kementerian Hukum Republik Indonesia"
        )
        self.assertEqual(self.certificate.year, "2026")

    def test_certificate_page(self):
        response = self.client.get(reverse("main:show_certificate"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certificate.html")
        self.assertContains(response, self.certificate.name)
        self.assertContains(response, self.certificate.issuer)
        self.assertContains(response, self.certificate.year)
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )