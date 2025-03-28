import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ThreadlyProject.settings')  # Replace with your project settings module
django.setup()

from Threadly.models import User, Thread, Post, Comments

def populate_data():

    user1 = User.objects.get_or_create(username="John",profilePictureURL="http://example.com/user1.jpg")[0]
    user2 = User.objects.get_or_create(username="Steven",profilePictureURL="http://example.com/user2.jpg")[0]
    user3 = User.objects.get_or_create(username="Jose",profilePictureURL="http://example.com/user3.jpg")[0]
    user4 = User.objects.get_or_create(username="Brad",profilePictureURL="http://example.com/user4.jpg")[0]
    user5 = User.objects.get_or_create(username="Dougie",profilePictureURL="http://example.com/user5.jpg")[0]
    user6 = User.objects.get_or_create(username="Stoney",profilePictureURL="http://example.com/user6.jpg")[0]

    thread1 = Thread.objects.get_or_create(title="Java",threadPhoto="http://example.com/thread1.jpg")[0]
    thread2 = Thread.objects.get_or_create(title="Python",threadPhoto="http://example.com/thread2.jpg")[0]
    thread3 = Thread.objects.get_or_create(title="Rust",threadPhoto="http://example.com/thread3.jpg")[0]
    thread4 = Thread.objects.get_or_create(title="C",threadPhoto="http://example.com/thread4.jpg")[0]
    thread5 = Thread.objects.get_or_create(title="C++",threadPhoto="http://example.com/thread5.jpg")[0]
    thread6 = Thread.objects.get_or_create(title="JavaScript",threadPhoto="http://example.com/thread6.jpg")[0]

    user1.follows.add(thread1,thread2,thread4)
    user2.follows.add(thread5,thread2)
    user3.follows.add(thread1,thread6)
    user4.follows.add(thread3)
    user5.follows.add(thread2)

    post1 = Post.objects.get_or_create(title="Java Issue",content="Java Issue Post content",photoContent="http://example.com/post1.jpg",threadID = thread1,userID=user1)[0]
    post2 = Post.objects.get_or_create(title="Python issue",content="Python issue post content",photoContent="http://example.com/post1.jpg",threadID=thread2,userID=user5)[0]

    comment1 = Comments.objects.get_or_create(commentContent="You have an issue in ln21",userID=user1,postID=post2)[0]

    print("Data populated successfully!")

def add_Thread(title, photo):
    thread = Thread.objects.get_or_create(title=title, threadPhoto=photo)[0]
    thread.save()
    return thread


populate_data()
