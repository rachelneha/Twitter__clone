from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class User(AbstractUser):
    date_of_Birth = models.DateField(null=True, blank=True)
    followers = models.ManyToManyField('self',related_name='following')
    following_count = models.IntegerField(null=True, blank=True)
    followers_count = models.IntegerField(null=True, blank=True)
    profile_Image = models.ImageField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        verbose_name= ('groups'),
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        verbose_name=('user permissions'),
        help_text=('Specific permissions for this user.'),
    )

    def __str__(self):
        return self.username

class Tweets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='tweeted_user')
    tweet = models.CharField(max_length=300)
    tweet_img = models.ImageField()
    Retweet_from = models.ForeignKey('self',on_delete=models.CASCADE,related_name='Retweet',null= True,blank = True)
    Like = models.ManyToManyField(User,related_name='likes',null= True,blank = True)


    def __str__(self):
        return self.tweet

class Comments(models.Model):
    text = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commented_user')
    tweet = models.ForeignKey(Tweets,on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self',on_delete=models.CASCADE)

    def __str__(self):
        return self.text
