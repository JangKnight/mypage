from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def main(request, month):
    res = ""
    month = month.lower()
    month = month.capitalize()
    print(month)
    if month == "January" or month == "Jan":
        res = "<h1>January</h1>"
    elif month == "February" or month == "Feb":
        res = "<h1>February</h1>"
    elif month == "March" or month == "Mar":
        res = "<h1>March</h1>"
    elif month == "April" or month == "Apr":
        res = "<h1>April</h1>"
    elif month == "May" or month == "May":
        res = "<h1>May</h1>"
    elif month == "June" or month == "Jun":
        res = "<h1>June</h1>"
    elif month == "July" or month == "Jul":
        res = "<h1>July</h1>"
    elif month == "August" or month == "Aug":
        res = "<h1>August</h1>"
    elif month == "September" or month == "Sep":
        res = "<h1>September</h1>"
    elif month == "October" or month == "Oct":
        res = "<h1>October</h1>"
    elif month == "November" or month == "Nov":
        res = "<h1>November</h1>"
    elif month == "December" or month == "Dec":
        res = "<h1>December</h1>"
    else:
        return HttpResponseNotFound("<h1>404 Not Found</h1>")
    return HttpResponse(res)

