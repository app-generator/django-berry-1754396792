# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Gender(models.Model):

    #__Gender_FIELDS__
    genderid = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Gender_FIELDS__END

    class Meta:
        verbose_name        = _("Gender")
        verbose_name_plural = _("Gender")


class County(models.Model):

    #__County_FIELDS__
    countyid = models.CharField(max_length=255, null=True, blank=True)
    countyname = models.TextField(max_length=255, null=True, blank=True)

    #__County_FIELDS__END

    class Meta:
        verbose_name        = _("County")
        verbose_name_plural = _("County")


class Family(models.Model):

    #__Family_FIELDS__
    unitid = models.CharField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Family_FIELDS__END

    class Meta:
        verbose_name        = _("Family")
        verbose_name_plural = _("Family")


class Member(models.Model):

    #__Member_FIELDS__
    image = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    idnumber = models.TextField(max_length=255, null=True, blank=True)
    mobileno = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    familyunit = models.ForeignKey(Family, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    #__Member_FIELDS__END

    class Meta:
        verbose_name        = _("Member")
        verbose_name_plural = _("Member")


class Contribution(models.Model):

    #__Contribution_FIELDS__
    memberno = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    referenceno = models.TextField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    #__Contribution_FIELDS__END

    class Meta:
        verbose_name        = _("Contribution")
        verbose_name_plural = _("Contribution")



#__MODELS__END
