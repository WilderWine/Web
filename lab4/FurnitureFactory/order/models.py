from django.db import models
from factory.models import Furniture, Client


class Order(models.Model):
    """
    model for order(deal)
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    complited = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Order {0}, {1}'.format(self.id, self.created)

    def get_total_cost(self):
        """
        getting total cost
        """
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
    model for order(deal)
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Furniture, related_name='order_items', on_delete=models.CASCADE)
    # cascade - 1 change - all change
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        """
        getting cost for estate
        """
        return self.price * self.quantity


from django.db import models

# Create your models here.
