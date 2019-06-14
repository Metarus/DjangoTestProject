from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.EntryView.as_view(), name='login'),
    path('submit/', views.submit, name='submit')
]