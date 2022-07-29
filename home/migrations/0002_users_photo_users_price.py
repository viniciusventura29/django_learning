# Generated by Django 4.0.6 on 2022-07-29 11:34

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='photo',
            field=stdimage.models.StdImageField(default=1, force_min_size=False, upload_to='photo/%y/%m/%d/', variations={'grande': (800, 800), 'medio': (500, 500), 'pequeno': (300, 300)}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]