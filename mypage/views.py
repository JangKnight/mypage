from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import render_to_string
def main(request):
    page = ""
    return me(request, page)

def me(request, page):
    if page == None or page == "":
        page = "home"
    else:
        page = page.lower()
    if page == "home":
        return render(request, "home.html")
    elif page == "about":
        return render(request, "about.html")
    elif page == "contact":
        return render(request, "contact.html")
    elif page == "journal":
        redirect_url = "/journal/"
        return HttpResponseRedirect(redirect_url)
    else:
        res = render_to_string("404.html")
        return HttpResponseNotFound(res)

