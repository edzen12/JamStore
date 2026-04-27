from django.views.generic import ListView
from apps.products.models import Jam


class HomeView(ListView): 
    model = Jam
    template_name = 'index.html'
    context_object_name = 'jams'

