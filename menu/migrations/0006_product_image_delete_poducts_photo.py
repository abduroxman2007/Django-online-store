# Generated by Django 4.0.4 on 2022-06-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_remove_product_image_poducts_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products_img'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Poducts_photo',
        ),
    ]
