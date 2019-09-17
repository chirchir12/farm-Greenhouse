import random
import os
import string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def unique_order_id_generator(instance):
    order_new_id =random_string_generator()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def resize_image(instance):
    pass


# this is function to get name and extension of image

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# this function generate random name of the image


def upload_image_path_products(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(
        new_filename=instance.slug, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=instance.category, final_filename=final_filename)


def upload_image_to_category(instance, filename):
    new_filename = random.randint(1, 76543776)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'category/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)

def upload_image_path_posts(instance, filename):
    name, ext = get_filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(
        new_filename=instance.slug, ext=ext)
    return "posts/{new_filename}/{final_filename}".format(new_filename=instance.slug, final_filename=final_filename)