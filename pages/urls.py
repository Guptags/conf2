from django.urls import path
from .views import HomePage, aboutview

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about', aboutview.as_view(), name='aboutt'),

]
