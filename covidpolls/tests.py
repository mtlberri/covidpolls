from django.test import TestCase

from .models import Child, Parent1


class ModelTests(TestCase):

    def test_child_has_a_parent(self):
        """every child should have a parent"""
        pass
