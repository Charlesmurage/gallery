from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photo_of_day(request):
    date = dt.date.today()

    return render(request, 'all-photos/today-photos.html',{"date":date,})

def previous_photos(request,past_date):

    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

        if date == dt.date.today():
            return redirect(photo_of_day)

        return render(request, 'all-photos/prev-photos.html',{"date":date,})

    day = convert_dates(date)
    html= f'''
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
