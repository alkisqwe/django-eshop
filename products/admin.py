from django.contrib import admin
from .models import Comment
from .models import Product
from .models import Wishlist

class CommentInline(admin.TabularInline):
    model = Comment


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Comment)
admin.site.register(Product,ProductAdmin)
admin.site.register(Wishlist)
