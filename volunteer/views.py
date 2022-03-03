from django.shortcuts import render


def home(request):
    """View for the student homepage."""
    return render(request, "volunteer/volunteer_home.html")
