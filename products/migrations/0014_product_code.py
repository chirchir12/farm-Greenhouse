# Generated by Django 2.2.4 on 2019-09-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20190928_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, help_text='rgs-py30', max_length=40, null=True),
        ),
    ]