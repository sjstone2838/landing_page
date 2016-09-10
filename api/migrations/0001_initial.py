# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(unique=True, max_length=200)),
                ('industry', models.CharField(default='', max_length=200, blank=True, choices=[('Business Process Outsourcing', 'Business Process Outsourcing'), ('Education', 'Education'), ('Financial Services', 'Financial Services'), ('Healthcare', 'Healthcare'), ('Hospitality', 'Hospitality'), ('Manufacturing', 'Manufacturing'), ('Retail', 'Retail'), ('Tech-Software', 'Tech-Software'), ('Tech-Hardware', 'Tech-Hardware'), ('Other', 'Other')])),
                ('employee_count', models.IntegerField(null=True, blank=True)),
                ('annual_hires', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
