# Generated by Django 2.1.11 on 2019-10-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20190813_1116'),
        ('design', '0008_auto_20190930_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='output_files',
            field=models.ManyToManyField(blank=True, to='db.File'),
        ),
    ]