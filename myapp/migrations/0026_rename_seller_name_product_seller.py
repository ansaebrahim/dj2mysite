# Generated by Django 4.1.2 on 2022-11-09 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_product_seller_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller_name',
            new_name='seller',
        ),
    ]