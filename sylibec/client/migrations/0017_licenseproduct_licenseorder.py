# Generated by Django 4.0.4 on 2022-09-29 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0016_learnerproduct_learnerorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licenseproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licensename', models.CharField(max_length=200)),
                ('licensedescription', models.TextField(blank=True, null=True)),
                ('licenseimage_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('licenseprice', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Licenseorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licensecreated', models.DateTimeField(auto_now_add=True)),
                ('licenseproduct', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.licenseproduct')),
            ],
        ),
    ]