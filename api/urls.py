from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductAPIView, CommentAPIView, CheckoutAPIView, WishlistAPIView, SavedAddressAPIView, SavedPaymentAPIView

router = SimpleRouter()
router.register("product",ProductAPIView,basename="product")
router.register("comment",CommentAPIView,basename="comment")
router.register("checkout",CheckoutAPIView,basename="checkout")
router.register("wishlist",WishlistAPIView,basename="wishlist")
router.register("saved-address",SavedAddressAPIView,basename="savedaddress")
router.register("saved-payment",SavedPaymentAPIView,basename="savedpayment")

urlpatterns = router.urls
