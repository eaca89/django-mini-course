from django.views.generic import TemplateView

# def messageView(request):
#     return render(request, 'home.html')

class MessageView(TemplateView):
    template_name = 'home.html'