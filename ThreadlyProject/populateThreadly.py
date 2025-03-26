import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ThreadlyProject.settings')  # Replace with your project settings module
django.setup()

from Threadly.models import User, Thread, Post, Comments

def populate_data():

    user1 = User.objects.create(username="John",profilePictureURL="http://example.com/user1.jpg")
    user2 = User.objects.create(username="Steven",profilePictureURL="http://example.com/user2.jpg")
    user3 = User.objects.create(username="Jose",profilePictureURL="http://example.com/user3.jpg")
    user4 = User.objects.create(username="Brad",profilePictureURL="http://example.com/user4.jpg")
    user5 = User.objects.create(username="Dougie",profilePictureURL="http://example.com/user5.jpg")
    user6 = User.objects.create(username="Stoney",profilePictureURL="http://example.com/user6.jpg")

    thread1 = Thread.objects.create(title="Java",threadPhoto="http://example.com/thread1.jpg")
    thread2 = Thread.objects.create(title="Python",threadPhoto="http://example.com/thread2.jpg")
    thread3 = Thread.objects.create(title="Rust",threadPhoto="http://example.com/thread3.jpg")
    thread4 = Thread.objects.create(title="C",threadPhoto="http://example.com/thread4.jpg")
    thread5 = Thread.objects.create(title="C++",threadPhoto="http://example.com/thread5.jpg")
    thread6 = Thread.objects.create(title="JavaScript",threadPhoto="http://example.com/thread6.jpg")

    user1.follows.add(thread1,thread2,thread4)
    user2.follows.add(thread5,thread2)
    user3.follows.add(thread1,thread6)
    user4.follows.add(thread3)
    user5.follows.add(thread2)

    post1 = Post.objects.create(title="Java Issue",content="Java Issue Post content",photoContent="http://example.com/post1.jpg",threadID = thread1,userID=user1)
    post2 = Post.objects.create(title="Python issue",content="Python issue post content",photoContent="http://example.com/post1.jpg",threadID=thread2,userID=user5)

    comment1 = Comments.objects.create(commentContent="You have an issue in ln21",userID=user1,postID=post2)

    print("Data populated successfully!")




populate_data()
