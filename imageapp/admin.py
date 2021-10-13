from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(mlimagemodel) 
admin.site.register(mlimage)
admin.site.register(Imagepath)



