from rest_framework import serializers
from products.models import Product, Comment, Wishlist
from accountsettings.models import SavedAddress, SavedPayment
from mycart.models import CheckoutModel
from dj_rest_auth.serializers import UserDetailsSerializer

class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = ('pk', 'username', 'email', 'type', 'profileimage', 'plan',)
        read_only_fields = ('pk',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("pk","owner","name","description","specifications","deliverytime","price","categorys","image","image2","image3")
        read_only_fields = ('pk',)

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutModel
        fields = ("pk","owner","name","email","phone","address","country","city","zipcode","shippingmethods","paymentmethods","cardnumber","cardname","cardexp","cardcvv","paypalemail","terms")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("pk","product","owner","body","stars","timeof","image1")
        read_only_fields = ('pk',)

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("pk","owner","product")
        read_only_fields = ('pk',)


class SavedAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedAddress
        fields = ("pk","owner","name","email","phone","address","country","city","zipcode")
        read_only_fields = ('pk',)
        
class SavedPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPayment
        fields = ("pk","owner","cardnumber","cardname","cardexp","cardcvv","paypalemail","type")
        read_only_fields = ('pk',)
