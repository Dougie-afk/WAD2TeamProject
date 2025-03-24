from django.db import models
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid


class Thread(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, blank=True)  # Added slug field
    threadID = models.AutoField(primary_key=True)
    threadPhoto = models.URLField()  # Thread image

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Thread.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{uuid.uuid4().hex[:4]}"  # Add random suffix
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True)
    userID = models.AutoField(primary_key=True)
    profilePictureURL = models.URLField(blank=True, null=True)
    follows = models.ManyToManyField(Thread, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)  # Required for login
    is_staff = models.BooleanField(default=False)  # Required for admin access
    is_superuser = models.BooleanField(default=False)  # Required for superuser

    objects = CustomUserManager()  

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username



class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=1000)
    photoContent = models.URLField(blank=True, null=True)
    postID = models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    threadID = models.ForeignKey(Thread, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title



class Comments(models.Model):
    commentContent = models.TextField(max_length=100)
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Comment by {self.userID.username if self.userID else 'Anonymous'} on {self.postID.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePictureURL = models.URLField(blank=True, null=True)
    follows = models.ManyToManyField(Thread, blank=True)

    def __str__(self):
        return self.user.username
