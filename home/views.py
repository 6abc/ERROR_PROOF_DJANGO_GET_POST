from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import MessageForm
import logging

logger = logging.getLogger(__name__)

@require_POST
def hello_world(request):
    try:
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']

            # Perform any other processing if needed

            response = render(request, 'home/hello_world.html', {'message': message})
            response['Content-Security-Policy'] = "default-src 'self'"
            response['X-Content-Type-Options'] = 'nosniff'

            return response
        else:
            # Form is invalid, return a response with errors
            return render(request, 'home/home.html', {'form': form}, status=400)

    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        return HttpResponse("An error occurred. Please try again later.", status=500)

def home(request):
    # Handle GET request to render the initial home.html page
    form = MessageForm()  # Create an empty form
    return render(request, 'home/home.html', {'form': form})