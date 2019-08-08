from django.contrib import admin
from .models import Neighbourhood,NeighbourhoodUser,Bussiness,Postcontent
# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(NeighbourhoodUser)
admin.site.register(Bussiness)
admin.site.register(Postcontent)