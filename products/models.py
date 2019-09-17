from django.db import models
import os
import random
from django.urls import reverse

from django.db.models.signals import pre_save
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from config.utils import (
    unique_slug_generator, 
    upload_image_to_category,
    upload_image_path_products

    )

class Category(models.Model):
    title = models.CharField(max_length=2000)
    slug  = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to=upload_image_to_category, null=True, blank=True)
    description = models.CharField(max_length=150, default='content')

    objects = models.Manager()


    class Meta:
        verbose_name_plural = 'Categories'

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products', kwargs={'slug': self.slug})

    def save(self):

        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((150, 100))

        # after modifications, save it to the output
        im.save(output, format='PNG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split(
            '.')[0], 'image/png', sys.getsizeof(output), None)

        super(Category, self).save()


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    # price       = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    image = models.ImageField(
        upload_to=upload_image_path_products, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

        # Resize/modify the image
        im = im.resize((150, 100))

        # after modifications, save it to the output
        im.save(output, format='PNG', quality=100)
        output.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.image.name.split(
            '.')[0], 'image/png', sys.getsizeof(output), None)

        super(Product, self).save()


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    phone   = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.subject





def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)
