from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(default='No Description')
    image = models.ImageField('Label')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("app:detail", kwargs={"pk": self.pk})

    def get_add_to_cart_url(self):
        return reverse("app:add-to-cart", kwargs={"pk": self.pk})



class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False, null=True, blank=False)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.item.name
    
    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')
    ordered = models.BooleanField(default=False, null=True, blank=False)
    date_added = models.DateTimeField(default=timezone.now())

    @property
    def get_cart_total(self):
        orderitems = self.items.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def __str__(self):
        return self.user.username

