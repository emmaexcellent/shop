# Generated by Django 4.1.3 on 2022-12-23 00:40

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_remove_variation_number_product_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumb_nail',
            field=models.ImageField(null=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='product_img/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='product_img/'),
        ),
    ]