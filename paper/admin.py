from django.contrib import admin
from .models import Folder,Files,Bookmark


# Register your models here.
admin.site.register(Folder)
admin.site.register(Files)
admin.site.register(Bookmark)