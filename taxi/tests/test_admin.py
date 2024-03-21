from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="test_driver",
            password="test_driver_password",
            license_number="test_license_number",
            first_name="test_first_name",
            last_name="test_last_name"
        )

    def test_driver_license_number_listed(self) -> None:
        url = reverse("admin:taxi_driver_changelist")
        url_response = self.client.get(url)
        self.assertContains(url_response, self.driver.license_number)

    def test_driver_detail_license_number_listed(self) -> None:
        url = reverse(
            "admin:taxi_driver_change",
            args=[self.driver.id]
        )
        url_response = self.client.get(url)
        self.assertContains(url_response, self.driver.license_number)
        self.assertContains(url_response, self.driver.first_name)
        self.assertContains(url_response, self.driver.last_name)