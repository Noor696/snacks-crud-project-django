from django.urls import path  # 1. import any thing built in django
from .views import HomePage,SnackListView, SnackDetailView  # 2. import from yout application

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('snacks', SnackListView.as_view(),name="snacks"),
    path('snacks/<pk>', SnackDetailView.as_view(),name="snacksdetail")
]

# snacks/<pk> : this dunamic path refer uniqe type of snackes 
# snacks/1 , snacks/2 , snacks/...