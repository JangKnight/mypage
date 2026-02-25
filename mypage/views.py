from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    page = ""
    return me(request, page)

def me(request, page):
    if page == None or page == "":
        page = "home"
    else:
        page = page.lower()
    if page == "home":
        title = "Home"
        content = "Welcome to my homepage!"
    elif page == "about":
        title = "About"
        content = "This is the about page."
    elif page == "contact":
        title = "Contact"
        content = "You can contact me at anthonysjhenry@icloud.com."
    elif page == "journal":
        redirect_url = "/journal/"
        return HttpResponse(f"<script>window.location.href='{redirect_url}';</script>")
    else:
        title = "Page Not Found"
        content = "Sorry, the page you are looking for does not exist."
    res = {"title": title, "content": content}
    return render(request, "main.html", res)

