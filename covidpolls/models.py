from django.db import models


class ParentChildPreference(models.Model):
    parent_first_name = models.CharField(max_length=100)
    parent_last_name = models.CharField(max_length=100)
    parent_email_address = models.EmailField(max_length=200)
    parent_phone = models.CharField(max_length=20)

    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    child_return_asap = models.BooleanField()
    child_date_return = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.child_first_name + ' ' + self.child_last_name

