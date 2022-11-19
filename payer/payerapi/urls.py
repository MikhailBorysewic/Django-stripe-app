from django.urls import path

from .views import ItemView, BuyItemView, IndexView, BuyOrder

urlpatterns = [
    path('item/<int:pk>', ItemView.as_view()),
    path('buy/<int:pk>', BuyItemView.as_view()),
    path('buy/order/<int:pk>', BuyOrder.as_view()),
    path('', IndexView.as_view()),
]
