from django.urls import path

from my_app import views


app_name = 'my-app'


urlpatterns = [
    path('foo/', views.my_view),
]
