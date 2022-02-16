from django.shortcuts import render

# Create your views here.

def home(request):
    """View for the student homepage."""
    return render(request, "volunteer/volunteer_home.html")