# Generated by Django 5.0.4 on 2024-05-07 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
