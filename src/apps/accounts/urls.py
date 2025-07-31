from django.urls import path

from accounts.views import AccountDetailView, register_view


urlpatterns = [
    path('register/', register_view, name='register'),
    path('detail/<int:pk>/', AccountDetailView.as_view(), name='account'),
]
