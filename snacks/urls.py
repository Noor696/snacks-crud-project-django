from django.urls import path  # 1. import any thing built in django
from .views import HomePage,SnackListView, SnackDetailView , SnackCreateView, SnackUpdateView, SnackDeleteView # 2. import from yout application

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('snacks', SnackListView.as_view(),name="snacks"),
    path('snacks/<int:pk>', SnackDetailView.as_view(),name="snack_detail"),
    path('create/', SnackCreateView.as_view(),name="snack_create"),
    path('update/<int:pk>', SnackUpdateView.as_view(),name="snack_update"),
    path('delete/<int:pk>', SnackDeleteView.as_view(),name="snack_delete"),
]

# snacks/<pk> : this dunamic path refer uniqe type of snackes 
# snacks/1 , snacks/2 , snacks/...