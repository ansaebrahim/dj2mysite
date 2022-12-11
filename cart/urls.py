from django.urls import path,include
# from .views import ProductUpdateView,ProductDeleteView,ProductCreateView
from . import views



urlpatterns = [
    path('cart/', views.ListCart.as_view(), name='list-carts'),
    path('cart/<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
    path('cart/create/', views.CreateCart.as_view(), name='create-cart'),
    path('cart/<int:pk>/update/', views.Updatecart.as_view(), name='update-cart'),
    path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),
]