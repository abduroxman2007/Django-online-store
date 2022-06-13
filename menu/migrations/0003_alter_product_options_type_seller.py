# Generated by Django 4.0.4 on 2022-06-07 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_seller_email'),
        ('menu', '0002_rename_seller_id_product_seller'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='type',
            name='seller',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.seller'),
        ),
    ]