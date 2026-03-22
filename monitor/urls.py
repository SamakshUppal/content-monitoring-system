from django.urls import path
from .views import *

urlpatterns = [
    path('keywords/', KeywordCreateView.as_view()),
    path('scan/', ScanView.as_view()),
    path('flags/', FlagListView.as_view()),
    path('flags/<int:pk>/', FlagUpdateView.as_view()),
]