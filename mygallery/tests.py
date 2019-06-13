from django.test import TestCase
from .models import Uploader,Pdetails, tags

# Create your tests here.

class UploaderTestCase(TestCase):
    def setUp(self):
        self.charles= Uploader(first_name = 'cahrles', last_name = 'maina', email = 'muragemaina09@gmil.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.charles,Uploader))

    def test_save_method(self):
        self.charles.save_uploader()
        uploaders = Uploader.objects.all()
        self.assertTrue(len(uploaders) > 0)
