from django.test import TestCase
from Threadly.models import User, Thread


class UserModelTests(TestCase):
    def setUp(self):
        self.thread1 = Thread.objects.create(title="Tech Group", threadPhoto="http://example.com/thread1.jpg")
        self.thread2 = Thread.objects.create(title="Surfing", threadPhoto="http://example.com/surf.jpg")

        self.abigail = User.objects.create_user(username="abigail", password="lawstudent123")
        self.william = User.objects.create_user(username="william", password="professor456", is_staff=True)
        self.nate = User.objects.create_user(username="nate", password="surfer789")

    def test_user_creation(self):
        self.assertEqual(self.abigail.username, "abigail")
        self.assertTrue(self.abigail.check_password("lawstudent123"))

        self.assertEqual(self.william.username, "william")
        self.assertTrue(self.william.check_password("professor456"))

        self.assertEqual(self.nate.username, "nate")
        self.assertTrue(self.nate.check_password("surfer789"))

    def test_user_roles(self):
        self.assertFalse(self.abigail.is_staff)
        self.assertTrue(self.william.is_staff)
        self.assertFalse(self.nate.is_staff)

    def test_user_follows_threads(self):
        self.abigail.follows.add(self.thread1)
        self.nate.follows.add(self.thread2)

        self.assertIn(self.thread1, self.abigail.follows.all())
        self.assertIn(self.thread2, self.nate.follows.all())

    def test_user_engagement(self):
        self.assertEqual(self.abigail.follows.count(), 1)
        self.assertEqual(self.william.follows.count(), 0)
        self.assertEqual(self.nate.follows.count(), 1)
