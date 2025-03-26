from django.test import TestCase
from Threadly.forms import UserRegistrationForm, ThreadForm


class FormsTests(TestCase):
    def test_valid_user_registration_form(self):
        form_data = {
            "username": "newuser",
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_registration_form(self):
        form_data = {
            "username": "",
            "password1": "pass",
            "password2": "diffpass",
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_thread_form(self):
        form_data = {
            "title": "New Tech Thread",
            "threadPhoto": "http://example.com/image.jpg"
        }
        form = ThreadForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_thread_form(self):
        form_data = {
            "title": "",
            "threadPhoto": "not_a_url"
        }
        form = ThreadForm(data=form_data)
        self.assertFalse(form.is_valid())
