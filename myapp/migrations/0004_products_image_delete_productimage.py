# Generated by Django 4.2.7 on 2025-06-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=None, upload_to='img/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
