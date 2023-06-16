from django.views.generic import ListView
from .models import Message
# def messageView(request):
#     return render(request, 'home.html')


class MessageView(ListView):
    model = Message
    template_name = 'home.html'
