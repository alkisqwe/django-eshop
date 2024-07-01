from rest_framework import generics
from products.models import Product, Comment, Wishlist
from accountsettings.models import SavedAddress, SavedPayment
from .serializers import ProductSerializer, CommentSerializer, CheckoutSerializer, WishlistSerializer, SavedAddressSerializer, SavedPaymentSerializer
from .permissions import ProductPermission, CommentPermission, CheckoutPermission, WishlistPermission, SavedAddressPermission, SavedPaymentPermission
from rest_framework import viewsets
from .paginations import ProductPagination, CommentPagination, CheckoutPagination, WishlistPagination, SavedAddressPagination, SavedPaymentPagination
from django.contrib.auth import get_user_model
from mycart.models import CheckoutModel
from accountsettings.models import SavedAddress, SavedPayment

class ProductAPIView(viewsets.ModelViewSet):
    permission_classes = (ProductPermission,)
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
        
    def get_queryset(self):
        page = self.request.GET.get('page', 1)
        searchquery = self.request.GET.get('search')
        usernamequery = self.request.GET.get('username')
        if(searchquery == None):
            searchqueryfinal = ""
        else:
            searchqueryfinal = searchquery
        prices = self.request.GET.get('prices')
        categories = self.request.GET.get('categorys')
        frominput = self.request.GET.get('frominput')
        toinput = self.request.GET.get('toinput')
        orderfin = "id"
        order = self.request.GET.get('order')
        if(order == None or order == "popular"):
            orderfin = "id"
        elif(order == "pricel"):
            orderfin = "price"
        elif(order == "priceh"):
            orderfin = "-price"
        if(usernamequery != None):
            tag = Product.objects.all().filter(owner=get_user_model().objects.get(pk=usernamequery)).order_by('id')
        if(categories == None and prices == None):
            tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
        elif(categories == None):
            if(prices == "AP"):
                tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "25"):
                tag = Product.objects.all().filter(price__lte=25,name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "2550"):
                tag = Product.objects.all().filter(price__range=(25,50),name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "50100"):
                tag = Product.objects.all().filter(price__range=(50,100),name__contains=searchqueryfinal).order_by(orderfin)
            elif(prices == "Other"):
                tag = Product.objects.all().filter(price__range=(frominput,toinput),name__contains=searchqueryfinal).order_by(orderfin)
        elif(prices == None):
            if(categories == None or categories == "SA"):
                tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
            else:
                tag = Product.objects.all().filter(categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
        else:
            if(categories == "SA"):
                if(prices == "AP"):
                    tag = Product.objects.all().filter(name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "25"):
                    tag = Product.objects.all().filter(price__lte=25,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "2550"):
                    tag = Product.objects.all().filter(price__range=(25,50),name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "50100"):
                    tag = Product.objects.all().filter(price__range=(50,100),name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "Other"):
                    tag = Product.objects.all().filter(price__range=(frominput,toinput),name__contains=searchqueryfinal).order_by(orderfin)
            else:
                if(prices == "AP"):
                    tag = Product.objects.all().filter(categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "25"):
                    tag = Product.objects.all().filter(price__lte=25,categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "2550"):
                    tag = Product.objects.all().filter(price__range=(25,50),categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "50100"):
                    tag = Product.objects.all().filter(price__range=(50,100),categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
                elif(prices == "Other"):
                    tag = Product.objects.all().filter(price__range=(frominput,toinput),categorys=categories,name__contains=searchqueryfinal).order_by(orderfin)
        return tag

class CommentAPIView(viewsets.ModelViewSet):
    permission_classes = (CommentPermission,)
    serializer_class = CommentSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        if(self.request.GET.get("productid") != None):
            return Comment.objects.all().filter(product=Product.objects.get(pk=self.request.GET.get("productid"))).order_by('id')
        else:
            return Comment.objects.all().order_by('id')
            
class CheckoutAPIView(viewsets.ModelViewSet):
    permission_classes = (CheckoutPermission,)
    serializer_class = CheckoutSerializer
    pagination_class = CheckoutPagination

    def get_queryset(self):
        return CheckoutModel.objects.all().filter(owner=self.request.user).order_by('id')

class WishlistAPIView(viewsets.ModelViewSet):
    permission_classes = (WishlistPermission,)
    serializer_class = WishlistSerializer
    pagination_class = WishlistPagination

    def get_queryset(self):
        return Wishlist.objects.all().filter(owner=self.request.user).order_by('id')

class SavedAddressAPIView(viewsets.ModelViewSet):
    permission_classes = (SavedAddressPermission,)
    serializer_class = SavedAddressSerializer
    pagination_class = SavedAddressPagination

    def get_queryset(self):
        return SavedAddress.objects.all().filter(owner=self.request.user).order_by('id')

class SavedPaymentAPIView(viewsets.ModelViewSet):
    permission_classes = (SavedPaymentPermission,)
    serializer_class = SavedPaymentSerializer
    pagination_class = SavedPaymentPagination

    def get_queryset(self):
        return SavedPayment.objects.all().filter(owner=self.request.user).order_by('id')

