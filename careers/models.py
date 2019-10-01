from django.db import models
from django.core.exceptions import ValidationError


# def validate_file_extension(value):
#     if value.file.content_type != 'application/pdf':
#         raise ValidationError('File format not Supported!!!!')





class Career(models.Model):
	
    fullname        = models.CharField(max_length=200)
    phone            = models.CharField(max_length=100)
    email            = models.EmailField(max_length=255)
    education        = models.CharField(max_length=255)
    cv               = models.FileField(upload_to='documents/CVs/')
    applying_for     = models.CharField(max_length=150)
    cover_letter = models.TextField()
    uploaded_at      = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.email

class JobDescription(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=False)
    objects = models.Manager()


    def __str__(self):
        return self.title