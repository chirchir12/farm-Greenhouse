import os
import random
from django.db import models


# this is function to get name and extension of image

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

# this function generate random name of the image


def upload_image_to(instance, filename):
	print(instance)
	print(filename)
	new_filename = random.randint(1, 76543776)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(
	    new_filename=new_filename, ext=ext)
	return 'about/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)


class About(models.Model):
	title       = models.CharField(max_length=100)
	image       = models.ImageField(upload_to=upload_image_to, null=True, blank=True)
	content     = models.TextField(default='content')
	

	def __str__(self):
		return self.title

    




