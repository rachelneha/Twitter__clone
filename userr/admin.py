from django.contrib import admin
from userr.models import User,Tweets,Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Tweets)
admin.site.register(Comments)