from django.db import models
from django.forms import ModelForm


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address_ln1 = models.CharField(max_length=100)
    address_ln2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state =  models.CharField(max_length=100)
    zip = models.IntegerField()
    email = models.EmailField(max_length=100)
    SalvageLogInquiryCheck = models.BooleanField(default=True, blank=True, null=True)
    MillingKilnInquiryCheck = models.BooleanField(default=True, blank=True, null=True)
    LumberyardInquiryCheck = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name

class SalvageLogInfo(models.Model):
    log_species = models.CharField(max_length=100)
    trunk_diameter = models.IntegerField()
    trunk_crotch_height = models.IntegerField()
    address_ln1 = models.CharField(max_length=100)
    address_ln2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state =  models.CharField(max_length=100)
    zip = models.IntegerField()

    def __str__(self):
        return self.log_species