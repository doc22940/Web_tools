from django.db import models
from db.models import File, Sample, Plate, Well

# Create your models here.


class Experiment(models.Model):
    PROJECT = (
        ('GF', 'GF_general'),
        ('SA', 'Sanguinarine'),
        ('MK', 'MoClo kit'),
        ('YK', 'Yeast CRISPR kit'),
    )
    STATUS = (
        ('On going', 'On going'),
        ('Completed', 'Completed'),
        ('Aborted', 'Aborted'),
        ('On hold', 'On hold'),
    )

    name = models.CharField(max_length=100)
    project = models.CharField(max_length=100, choices=PROJECT, blank=True)
    author = models.CharField(max_length=30)
    # workflow = models.ManyToManyField(Step, blank=True)
    status = models.CharField(default='On going', max_length=30, choices=STATUS, blank=True)
    input_file = models.FileField(upload_to='design/', max_length=10000, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    SCRIPTS = (
        ('Moclo', 'Moclo'),
        ('Normalization', 'Normalization'),
        ('Spotting', 'Spotting'),
        ('PCR', 'PCR'),
    )

    INSTRUMENTS = (
        ('Echo', 'Echo'),
        ('Mantis', 'Mantis'),
        ('Biomek', 'Biomek'),
        ('QIAquick96', 'QIAquick96'),
        ('Qpix', 'Qpix'),
        ('Thermal Cycler', 'Thermal Cycler'),
        ('Fragment Analyzer', 'Fragment Analyzer'),
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    script = models.CharField(max_length=30, choices=SCRIPTS, blank=True)
    instructions = models.CharField(max_length=10000, blank=True)
    instrument = models.CharField(max_length=100, blank=True)
    input_file = models.ManyToManyField(File, blank=True, related_name='script_input_files')
    output_files = models.ManyToManyField(File, blank=True, related_name='script_output_files')
    input_plates = models.ManyToManyField(Plate, blank=True, related_name='input_plates')
    output_plates = models.ManyToManyField(Plate, blank=True, related_name='output_plates')
    status_run = models.BooleanField(default=False)
    # relationship = table with relatioship between plate/well source and destination including samples, volume and concentration.
    experiment = models.ForeignKey(Experiment, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name