# Generated by Django 3.2.9 on 2021-11-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_page_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]