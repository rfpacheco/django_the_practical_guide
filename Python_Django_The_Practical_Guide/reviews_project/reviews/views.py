from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request):
    if request.method == "POST":
        enter_username = request.POST["username"]

        if enter_username == "" or len(enter_username) >= 100:
            return render(request, "reviews/review.html",
                          {"has_error" : True})

        print(enter_username)
        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")