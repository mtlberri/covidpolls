from django.db import models


class ParentChildPreference(models.Model):
    parent_first_name = models.CharField(max_length=100, blank=False)
    parent_last_name = models.CharField(max_length=100, blank=False)
    parent_email_address = models.EmailField(max_length=200, blank=False)
    parent_phone = models.CharField(max_length=20, blank=False)

    child_first_name = models.CharField(max_length=100, blank=False)
    child_last_name = models.CharField(max_length=100, blank=False)
    child_return_asap = models.BooleanField(blank=False)
    child_date_return = models.DateField(blank=True )

    def __str__(self):
        return self.child_first_name + ' ' + self.child_last_name

