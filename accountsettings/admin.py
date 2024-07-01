from django.contrib import admin
from .models import SavedAddress
from .models import SavedPayment

admin.site.register(SavedAddress)
admin.site.register(SavedPayment)
