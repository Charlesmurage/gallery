from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to my gallery')

def photo_of_day(request):
    date = dt.date.today()

    day = convert_dates(date)
    html = f'''
    <html>
    <body>
    <h1> Photo for {day} {date.day}-{date.month}-{date.year}</h1>
    </body>
    </html>
    '''
    return HttpResponse(html)

def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['monday','tuesday','wednesday','thursday','friday','saturday',"sunday"]

    day = days[day_number]
    return day
