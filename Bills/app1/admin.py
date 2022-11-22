from django.contrib import admin
from . models import Billing

# Register your models here.
@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display= ("id","first_name","last_name","address","email","mobile","Payable_amt","item",'qty')
