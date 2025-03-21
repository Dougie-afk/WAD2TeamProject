import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ThreadlyProject.settings')  # Replace with your project settings module
django.setup()

from Threadly.models import User, Thread, Post, Comments


def populate_data():
    # Create Users
    user1 = User.objects.create(username="user1", profilePictureURL="http://example.com/user1.jpg", password="password123")
    user2 = User.objects.create(username="user2", profilePictureURL="http://example.com/user2.jpg", password="password456")
    
    # Create Threads
    thread1 = Thread.objects.create(title="Django Discussion", threadPhoto="http://example.com/thread1.jpg")
    thread2 = Thread.objects.create(title="Python Programming", threadPhoto="http://example.com/thread2.jpg")
    
    # Users following threads
    user1.follows.add(thread1, thread2)
    user2.follows.add(thread1)

    # Create Posts
    post1 = Post.objects.create(title="Django Models", content="This post is about Django models.", photoContent="http://example.com/post1.jpg", threadID=thread1, UserID=user1)
    post2 = Post.objects.create(title="Python Lists", content="This post explains Python lists.", photoContent="http://example.com/post2.jpg", threadID=thread2, UserID=user2)

    # Create Comments
    comment1 = Comments.objects.create(commentContent="Great explanation on Django!", postID=post1, userID=user2)
    comment2 = Comments.objects.create(commentContent="I love Python!", postID=post2, userID=user1)

    print("Data populated successfully!")

populate_data()
