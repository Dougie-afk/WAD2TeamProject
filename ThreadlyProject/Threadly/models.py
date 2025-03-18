from django.db import models
#on_delete=models.SET_NULL, null=True, blank=True 
#Means will NOT DELETE RELATED CONTENT
#E.G if User is deleted, it wil not delete their posts
#But mark them as USER_DELETED in threads.

#on_delete=models.CASCADE does the opposite,
#deletes all related content e.g
#If thread is deleted, all posts are too 

class Thread(models.Model):
    title = models.CharField(max_length=32)
    threadID = models.AutoField(primary_key=True)
    threadPhoto = models.URLField()

    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=32)
    userID = models.AutoField(primary_key=True)
    profilePictureURL = models.URLField()
    follows = models.ManyToManyField(Thread, blank=True)
    password= models.CharField(max_length=128)

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



    



    

