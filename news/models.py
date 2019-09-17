from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from config.utils import unique_slug_generator, upload_image_path_posts

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    image   = models.ImageField(blank=True, upload_to=upload_image_path_posts, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
       
        return reverse('posts-detail', kwargs={'slug': self.slug})


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, sender=Post)
