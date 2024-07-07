from django.shortcuts import render

def get_site(request):
    return render(request, "website/landingPage.html")