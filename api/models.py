from __future__ import unicode_literals

from django.db import models

class TimeStampedModel(models.Model):
    # An abstract base class model that rovides self-updating 'created' and
    # 'modified' fields.
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

ORGANIZATION_INDUSTRY_CHOICES = (
    ('Business Process Outsourcing', 'Business Process Outsourcing'),
    ('Education', 'Education'),
    ('Financial Services', 'Financial Services'),
    ('Healthcare', 'Healthcare'),
    ('Hospitality', 'Hospitality'),
    ('Manufacturing', 'Manufacturing'),
    ('Retail', 'Retail'),
    ('Tech-Software', 'Tech-Software'),
    ('Tech-Hardware', 'Tech-Hardware'),
    ('Other', 'Other'),
)

class Registrant(TimeStampedModel):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False, unique=True)
    industry = models.CharField(max_length=200,
                                choices=ORGANIZATION_INDUSTRY_CHOICES,
                                blank=True,
                                default='')
    employee_count = models.IntegerField(null=True, blank=True)
    annual_hires = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)
