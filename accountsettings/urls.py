from django.urls import path
from .views import AccountSettingsView, SecuritySettingsView, BillingSettingsView, MyProductsView, MyWishlistView, BillSettingsView, AddAddressView, EditAddressView, AddPaymentView, EditPaymentView, PlanView

urlpatterns = [
    path("profile-settings", AccountSettingsView.as_view(), name="accountsettings"),
    path("security-settings", SecuritySettingsView.as_view(), name="securitysettings"),
    path("billing-settings", BillingSettingsView.as_view(), name="billingsettings"),
    path("bill-settings", BillSettingsView.as_view(), name="billsettings"),
    path("my-products", MyProductsView.as_view(), name="myproducts"),
    path("my-wishlist", MyWishlistView.as_view(), name="mywishlist"),
    path("add-address", AddAddressView.as_view(), name="addaddress"),
    path("edit-address/<int:pk>", EditAddressView.as_view(), name="editaddress"),
    path("add-payment", AddPaymentView.as_view(), name="addpayment"),
    path("edit-payment/<int:pk>", EditPaymentView.as_view(), name="editpayment"),
    path("plan/<int:pk>", PlanView.as_view(), name="plan"),
]
