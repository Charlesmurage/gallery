from django.test import TestCase
from .models import Uploader,Pdetails, tags

# Create your tests here.

class UploaderTestCase(TestCase):
    def setUp(self):
        self.charles= Uploader(first_name = 'cahrles', last_name = 'maina', email = 'muragemaina09@gmil.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.charles,Uploader))
