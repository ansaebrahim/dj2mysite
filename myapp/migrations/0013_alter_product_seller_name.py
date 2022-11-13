# Generated by Django 4.1.2 on 2022-11-09 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0012_alter_product_seller_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
