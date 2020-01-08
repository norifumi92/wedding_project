from django.contrib import admin
#import Model
from my_app.models import Attendee

#Configure Admin title
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Nori&Amira Wedding Admin Page!"

# Register your models here.
admin.site.register(Attendee)