# Generated by Django 2.2.4 on 2019-09-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='automatic',
            field=models.BooleanField(default=False, help_text='manual or automatic'),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, help_text='eg red, green blue', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='connection',
            field=models.CharField(blank=True, help_text='eg 2 Threads', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='controller',
            field=models.CharField(blank=True, help_text='for solar pumps', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dimension',
            field=models.CharField(blank=True, help_text="eg 11'W x 21.22'L x 1.5'D", max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='frequency',
            field=models.CharField(blank=True, help_text='for booster pumps, eg 50hz, 2.37A, 0.5HP', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fuel_consumption',
            field=models.CharField(blank=True, help_text='eg 4.68ltrs/l', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fuel_type',
            field=models.CharField(blank=True, help_text='eg gasoline', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.CharField(blank=True, help_text='eg 100m', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(blank=True, help_text='manufactorer, eg. Tiger', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, help_text='eg aluminum + brass', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='max_current',
            field=models.CharField(blank=True, help_text='eg 10A/16A', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='max_flow',
            field=models.CharField(blank=True, help_text='eg 92-15l/min', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='max_head',
            field=models.CharField(blank=True, help_text='eg 23m', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='outlet_inlet',
            field=models.CharField(blank=True, help_text='eg 2', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='power',
            field=models.CharField(blank=True, help_text='horse power', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pressure',
            field=models.CharField(blank=True, help_text='eg 1.5 bar-10 bar', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quality',
            field=models.CharField(blank=True, help_text='for solar panels, high quality junction box with diode protection', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='radius',
            field=models.CharField(blank=True, help_text='eg springer coverage 18=28m', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, help_text="eg '1X1'", max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sunction_head',
            field=models.CharField(blank=True, help_text='eg 8m', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tank_capcity',
            field=models.CharField(blank=True, help_text='eg capacity of 0.6 L', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='texture',
            field=models.CharField(blank=True, help_text=' for solar panels, eg. glass', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='thickness',
            field=models.CharField(blank=True, help_text='eg for pipes, eg 5mm', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='voltage',
            field=models.CharField(blank=True, help_text='for solar pumps, eg. 24V DC', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='watts',
            field=models.CharField(blank=True, help_text='for solar panels, eg. 100W', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, help_text='eg 180kgs', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(blank=True, help_text='model type (for generators)', max_length=100, null=True),
        ),
    ]
