from django.db import models
from django.db.models.signals import pre_save
from config.utils import  unique_slug_generator
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug  = models.SlugField(null=True, blank=True, unique=True)
    main_project_image = models.ImageField(upload_to='projects/image')
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       
        return reverse('project-detail', kwargs={'slug': self.slug})


class OtherImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='otherimages')
    image = models.ImageField(upload_to='projects/image', null=True, blank=True)


def project_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(project_pre_save_receiver, sender=Project)