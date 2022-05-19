from django.contrib import admin
from .models import User,Comment,Order,Shipment,Payment
# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Shipment)
admin.site.register(Payment)

