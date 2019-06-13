from django.shortcuts import render
from django.http import HttpResponse,Http404
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
    <h1> Photos uploaded on {day} {date.day}-{date.month}-{date.year}</h1>
    </body>
    </html>
    '''
    return HttpResponse(html)

def previous_photos(request,past_date):

    try:
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()

    day = convert_dates(date)
    html= f'''

     day = convert_dates(date)
    html = f'''
    <html>
    <body>
    <h1> Photos uploaded on {day} {date.day}-{date.month}-{date.year}</h1>
    </body>
    </html>
    '''
    return HttpResponse(html)


def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['monday','tuesday','wednesday','thursday','friday','saturday',"sunday"]

    day = days[day_number]
    return day
