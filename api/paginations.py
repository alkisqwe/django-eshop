from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 3
    
class CommentPagination(PageNumberPagination):
    page_size = 5

class CheckoutPagination(PageNumberPagination):
    page_size = 3

class WishlistPagination(PageNumberPagination):
    page_size = 3

class SavedAddressPagination(PageNumberPagination):
    page_size = 1

class SavedPaymentPagination(PageNumberPagination):
    page_size = 2
