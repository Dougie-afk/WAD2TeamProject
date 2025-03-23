from django.db import models
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
import uuid
#on_delete=models.SET_NULL, null=True, blank=True 
#Means will NOT DELETE RELATED CONTENT
#E.G if User is deleted, it wil not delete their posts
#But mark them as USER_DELETED in threads.

#on_delete=models.CASCADE does the opposite,
#deletes all related content e.g
#If thread is deleted, all posts are too 

class Thread(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, blank=True)# Added slug field
    threadID = models.AutoField(primary_key=True)
    threadPhoto = models.URLField()#The login attempts to update the user's last login field
    
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
    
class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    userID = models.AutoField(primary_key=True)
    profilePictureURL = models.URLField()
    password = models.CharField(max_length=128,default="defaultpassword")#Add password field and set default password
    
    follows = models.ManyToManyField(Thread, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False


    def __str__(self):
        return self.username
    
class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=1000)
    photoContent = models.URLField()
    postID = models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    threadID = models.ForeignKey(Thread, on_delete=models.CASCADE)
    UserID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    commentContent = models.TextField(max_length=100)
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Comment by {self.userID.username} on {self.postID.title}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePictureURL = models.URLField(blank=True, null=True)
    follows = models.ManyToManyField('Thread', blank=True)

    def __str__(self):
        return self.user.username    



    



    

