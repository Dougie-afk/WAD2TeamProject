from django.test import TestCase, Client
from django.urls import reverse
from Threadly.models import User, Thread


class ViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.thread = Thread.objects.create(title="Tech Group", threadPhoto="http://example.com/thread1.jpg")
        self.user = User.objects.create_user(username="testuser", password="securepass123")

    def test_thread_list_view(self):
        response = self.client.get(reverse("thread_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tech Group")

    def test_thread_detail_view(self):
        response = self.client.get(reverse("thread_detail", args=[self.thread.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tech Group")

    def test_user_can_follow_thread(self):
        self.client.login(username="testuser", password="securepass123")
        response = self.client.post(reverse("follow_thread", args=[self.thread.id]))
        self.user.refresh_from_db()
        self.assertIn(self.thread, self.user.follows.all())

    def test_user_can_unfollow_thread(self):
        self.client.login(username="testuser", password="securepass123")
        self.user.follows.add(self.thread)
        response = self.client.post(reverse("unfollow_thread", args=[self.thread.id]))
        self.user.refresh_from_db()
        self.assertNotIn(self.thread, self.user.follows.all())
