from django.shortcuts import render
from django.http import HttpResponse

def me(request, page):
    if page == None or page == "":
        page = "home"
    if page == "home":
        title = "Home"
        content = "Welcome to my homepage!"
    elif page == "about":
        title = "About"
        content = "This is the about page."
    elif page == "contact":
        title = "Contact"
        content = "You can contact me at anthonysjhenry@icloud.com."
    else:
        title = "Page Not Found"
        content = "Sorry, the page you are looking for does not exist."
    return render(request, "main.html", {"title": title, "content": content})

