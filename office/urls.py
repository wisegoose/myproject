from django.urls import path

from office import views


urlpatterns = [
    path('', views.office, name='office'),
]
