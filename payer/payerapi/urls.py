from django.urls import path

from .views import ItemView, BuyItemView, IndexView

urlpatterns = [
    path('item/<int:pk>', ItemView.as_view()),
    path('buy/<int:pk>', BuyItemView.as_view()),
    path('', IndexView.as_view()),
]
