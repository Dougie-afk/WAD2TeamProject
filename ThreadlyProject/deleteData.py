import os
import django

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ThreadlyProject.settings")
django.setup()

from Threadly.models import User, Thread, Post, Comments  # import your models

def clear_data():
    # Delete all data from the models
    User.objects.all().delete()
    Thread.objects.all().delete()
    Post.objects.all().delete()
    Comments.objects.all().delete()
    
    print("All data has been deleted.")

if __name__ == "__main__":
    clear_data()
