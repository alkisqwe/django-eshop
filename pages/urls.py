from django.urls import path
from .views import HomePageView, ProductPageView, AddProductView, EditProductView, CartView, CheckoutView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("product/<int:pk>", ProductPageView.as_view(), name="productdetails"),
    path("add-product/", AddProductView.as_view(), name="addproduct"),
    path("edit-product/<int:pk>", EditProductView.as_view(), name="editproduct"),
    path("cart", CartView.as_view(), name="cart"),
    path("checkout", CheckoutView.as_view(), name="checkout"),
]
