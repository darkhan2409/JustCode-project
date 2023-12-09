from .views import *
from django.urls import path


urlpatterns = [
    path('sign_up/', SignUpApiView.as_view()),
    path('sign_in/', SignIn.as_view()),
    path('sign_out/', SignOut.as_view()),

    path('profile/', Profile.as_view()),
]
