# Generated by Django 4.0.4 on 2022-09-28 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_rename_created_learnersorder_createdl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicleproduct',
            old_name='description',
            new_name='ldescription',
        ),
        migrations.RenameField(
            model_name='vehicleproduct',
            old_name='image_url',
            new_name='limage_url',
        ),
        migrations.RenameField(
            model_name='vehicleproduct',
            old_name='name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='vehicleproduct',
            old_name='price',
            new_name='lprice',
        ),
    ]
