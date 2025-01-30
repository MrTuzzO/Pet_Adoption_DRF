from django.urls import path
from .views import CustomConfirmEmailView, ProfileView

urlpatterns = [
    path("registration/account-confirm-email/<str:key>/", CustomConfirmEmailView.as_view(), name="account_confirm_email",),
    path('profile/', ProfileView.as_view(), name='profile'),
]
