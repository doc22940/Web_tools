# Generated by Django 2.1.11 on 2019-09-18 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_experiment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='status',
            field=models.CharField(blank=True, choices=[('On going', 'On going'), ('Completed', 'Completed'), ('Aborted', 'Aborted'), ('On hold', 'On hold')], default='On going', max_length=30),
        ),
        migrations.AlterField(
            model_name='step',
            name='instrument',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
