# Generated by Django 3.2.6 on 2021-09-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210901_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='big_image',
            field=models.ImageField(help_text='maximale Bildauflösung 1200x800', upload_to='images/carousel', verbose_name='bild groß'),
        ),
    ]
