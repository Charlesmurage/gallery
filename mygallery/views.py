from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Pdetails

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def photo_of_day(request):
    date = dt.date.today()
    mygallery = Pdetails.todays_photos()

    return render(request, 'all-photos/today-photos.html',{"date":date,"mygallery":mygallery})

def previous_photos(request,past_date):

    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photo_of_day)

    mygallery = Pdetails.days_photos(date)
    return render(request, 'all-photos/prev-photos.html',{"date":date,"mygallery":mygallery})


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

def search_results(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Pdetails.search_by_title(search_term)

        message = f"{search_term}"

        return render(request,'all-photos/search.html',{"message":message,"photos":searched_photos})

    else:
        message = "You havent searched for any term"

        return render(request,'all-photos/search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = Pdetails.objects.get(id = photo_id)

    except DoesNotExist:
        raise Http404()

    return render(request,"all-photos/photo.html", {"photo":photo})
