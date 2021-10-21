from django.db import models

# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Folder"
        verbose_name_plural="Folders"


class Files(models.Model):
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE)
    fileName = models.CharField(max_length=100)
    data = models.FileField(upload_to='files/')

    def __str__(self):
        return self.fileName

    class Meta:
        verbose_name="File"
        verbose_name_plural="Files"

class Bookmark(models.Model):
    name = models.CharField(max_length=100)
    files = models.ForeignKey(Files,on_delete=models.CASCADE)

    def __str__(self):
        return self.name