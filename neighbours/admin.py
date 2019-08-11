from django.contrib import admin
from .models import Neighbourhood,CustomUser,Bussiness,Post
# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(CustomUser)
admin.site.register(Bussiness)
admin.site.register(Post)
