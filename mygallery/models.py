from django.db import models
import datetime as dt

# Create your models here.
class Uploader(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length =10,blank = True)


    def __str__(self):
        return self.first_name

    def save_uploader(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Pdetails(models.Model):
    title = models.CharField(max_length =60)
    details = models.TextField()
    uploader = models.ForeignKey(Uploader)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        mygallery = cls.objects.filter(pub_date__date = today)

        return mygallery

    @classmethod
    def days_photos(cls,date):
        mygallery = cls.objects.filter(pub_date__date = date)
        return mygallery