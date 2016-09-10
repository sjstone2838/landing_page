# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='industry',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[('Business Process Outsourcing', 'Business Process Outsourcing'), ('Education', 'Education'), ('Financial Services', 'Financial Services'), ('Healthcare', 'Healthcare'), ('Hospitality', 'Hospitality'), ('Manufacturing', 'Manufacturing'), ('Retail', 'Retail'), ('Tech-Software', 'Tech-Software'), ('Tech-Hardware', 'Tech-Hardware'), ('Other', 'Other')]),
        ),
    ]
