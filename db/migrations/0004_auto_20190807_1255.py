# Generated by Django 2.1.11 on 2019-08-07 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20190806_1604'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='well',
            unique_together={('name', 'plate')},
        ),
    ]
