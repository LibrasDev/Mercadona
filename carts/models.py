from django.db import models
from store.models import Product, Variation
from accounts.models import Account

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def tax_percent(self):
        tax_percent = self.product.tax_percent
        return tax_percent
    
    def tax_percent_price(self):
        tax_percent = self.product.tax_percent
        percent_price_total = (self.product.price * tax_percent) / 100
        tax_percent_price = self.product.price - percent_price_total
        return tax_percent_price

    def sub_total_2f(self):
        tax_percent = self.product.tax_percent
        
        if tax_percent != 0:
            percent_price = (self.product.price * tax_percent) / 100
            percent_price_total = self.product.price - percent_price
        else:
            percent_price_total = self.product.price
            
        sub_total = percent_price_total * self.quantity
        return("%.2f" % sub_total)
    
    def __unicode__(self):
        return self.product