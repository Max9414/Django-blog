from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('created_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
