# Generated by Django 2.2 on 2019-04-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_category_cat_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
