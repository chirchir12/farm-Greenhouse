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
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length=2000)
    slug  = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to=upload_image_to_category, null=True, blank=True)
    description = models.TextField(max_length=300, default='content')

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
    type   = models.CharField(max_length=40, blank=True, null=True, help_text="type of the product")
    slug = models.SlugField(blank=True, unique=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True, help_text="manufactorer, eg. Tiger")
    power = models.CharField(max_length=40, blank=True, null=True, help_text="horse power")
    model = models.CharField(max_length=100, null=True, blank=True, help_text="model type (for generators)")
    max_head = models.CharField(max_length=40, blank=True, null=True, help_text="eg 23m")
    sunction_head = models.CharField(max_length=40, blank=True, null=True, help_text="eg 8m")
    outlet_inlet = models.CharField(max_length=40, blank=True, null=True, help_text="eg 2")
    automatic_or_manual = models.CharField(max_length=40, blank=True, null=True, help_text="manual or automatic")
    max_flow = models.CharField(max_length=40, blank=True, null=True, help_text="eg 92-15l/min")
    controller = models.CharField(max_length=100, blank=True, null=True, help_text="for solar pumps")
    voltage = models.CharField(max_length=100, blank=True, null=True, help_text="for solar pumps, eg. 24V DC")
    texture = models.CharField(max_length=100, blank=True, null=True, help_text=" for solar panels, eg. glass")
    quality = models.CharField(max_length=100, blank=True, null=True, help_text="for solar panels, high quality junction box with diode protection")
    watts = models.CharField(max_length=100, blank=True, null=True, help_text="for solar panels, eg. 100W")
    frequency = models.CharField(max_length=100, blank=True, null=True, help_text="for booster pumps, eg 50hz, 2.37A, 0.5HP")
    size = models.CharField(max_length=40, blank=True, null=True, help_text="eg '1X1'")
    fuel_consumption = models.CharField(max_length=100, blank=True, null=True, help_text="eg 4.68ltrs/l")
    weight = models.CharField(max_length=40, blank=True, null=True, help_text="eg 180kgs")
    pressure = models.CharField(max_length=100, blank=True, null=True, help_text="eg 1.5 bar-10 bar")
    max_current = models.CharField(max_length=100, blank=True, null=True, help_text="eg 10A/16A")
    # sprinklers
    material = models.CharField(max_length=100, blank=True, null=True, help_text="eg aluminum + brass")
    radius = models.CharField(max_length=100, blank=True, null=True, help_text="eg springer coverage 18=28m")
    connection = models.CharField(max_length=40, blank=True, null=True, help_text="eg 2 Threads")
    #farm machinery
    fuel_type = models.CharField(max_length=100, blank=True, null=True, help_text="eg gasoline")
    tank_capcity = models.CharField(max_length=40, blank=True, null=True, help_text="eg capacity of 0.6 L")
    #pipes
    thickness = models.CharField(max_length=40, blank=True, null=True, help_text="eg for pipes, eg 5mm")
    color = models.CharField(max_length=40, blank=True, null=True, help_text="eg red, green blue")
    length = models.CharField(max_length=40, blank=True, null=True, help_text="eg 100m")
    dimension = models.CharField(max_length=40, blank=True, null=True, help_text="eg 11'W x 21.22'L x 1.5'D")

    
    description = models.TextField( null=True, blank=True)
    # price       = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    image = models.ImageField(
        upload_to=upload_image_path_products)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})



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
