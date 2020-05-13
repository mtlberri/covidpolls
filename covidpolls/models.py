from django.db import models


class Parent1(models.Model):
    parent1_first_name = models.CharField(max_length=100, blank=False)
    parent1_last_name = models.CharField(max_length=100, blank=False)
    parent1_email_address = models.EmailField(max_length=200, blank=False)
    parent1_phone = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.parent1_first_name + ' ' + self.parent1_last_name


class Child(models.Model):
    parent1 = models.ForeignKey(Parent1, on_delete=models.CASCADE)
    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    child_return_asap = models.BooleanField(default=True)
    child_date_return = models.DateField(default='2020-01-01', blank=True)

    def __str__(self):
        return self.child_first_name + ' ' + self.child_last_name
