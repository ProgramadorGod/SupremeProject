# Generated by Django 4.2.1 on 2023-08-22 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_alter_category_prod_options_product_pcreated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PCreated',
            new_name='Created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PUpdated',
            new_name='Updated',
        ),
    ]
