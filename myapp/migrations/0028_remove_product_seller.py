# Generated by Django 4.1.2 on 2022-11-09 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
    ]