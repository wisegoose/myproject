from django.urls import path
from django.views.generic import ListView

from office.models import Workspace


urlpatterns = [
    path('', ListView.as_view(queryset=Workspace.objects.all()),
         template_name='search/search.html')
]
