
from django.test import TestCase, Client
from django.urls import reverse
import Faker
from .models import Area
from userapp.models import Applicant


# Create your tests here.
class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_index(self):
        res = self.client.get(reverse('parserHHapp:index'))
        self.assertEqual(res.status_code, 200)

    def test_area(self):
        res = self.client.get(reverse('parserHHapp:area_list'))
        self.assertEqual(res.status_code, 200)
        fake = Faker
        Applicant.objects.create_user(username=fake.name, email='test@test.ru', password='1234567tt')
        self.client.login(username=fake.name, password='1234567tt')

