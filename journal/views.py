from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

months = {
    "January": "January",
    "February": "February",
    "March": "March",
    "April": "April",
    "May": "May",
    "June": "June",
    "July": "July",
    "August": "August",
    "September": "September",
    "October": "October",
    "November": "November",
    "December": "December"
}

def journals_by_month(request, month):
    res = ""
    month = month.lower()
    month = month.capitalize()
    if month in months:
        res = f"<h1>{months[month]}</h1>"
    else:
        return HttpResponseNotFound("<h1>404 Not Found</h1>")
    return HttpResponse(res)

def journals_by_number(request, month):
    res = ""
    if month < 1 or month > 12:
        return HttpResponseNotFound("<h1>404 Not Found</h1>")
    else:
        month_name = list(months.keys())[month - 1]
        res = f"<h1>{months[month_name]}</h1>"
    return HttpResponse(res)