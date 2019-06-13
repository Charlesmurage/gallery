from django.test import TestCase
from .models import Uploader,Pdetails, tags
import datetime as dt

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

class PdetailsTestClass(TestCase):
    def setUp(self):
        self.charles= Uploader(first_name = 'charles', last_name= 'maina', email = 'muragemaina09@gmail.com')
        self.charles.save_uploader()

        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_photo= Pdetails(title = 'Test Pdetails',uploader = self.charles)
        self.new_photo.save()

        self.new_photo.tags.add(self.new_tag)

    def tearDown(self):
        Uploader.objects.all().delete()
        tags.objects.all().delete()
        Pdetails.objects.all().delete()

    def test_get_photos_today(self):
        today_photos = Pdetails.todays_photos()
        self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()

        photos_by_date = Pdetails.days_photos(date)
        self.assertTrue(len(photos_by_date) == 0)

