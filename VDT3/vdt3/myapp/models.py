from django.db import models
from datetime import datetime, timedelta

class Order(models.Model):
    # Field defining  the order
    customer = models.CharField(max_length=255)
    order_date = models.DateField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    """Note: Seed data for orders.json is not generated manually, external sources are used."""

    @classmethod
    # Calculate the top 5 customers with the highest total amount
    def get_top_customers(cls):
        # Calculate date 6 months ago from current date
        six_months_ago = datetime.now() - timedelta(days=180)
        # Query orders 
        top_customers = cls.objects.filter(order_date__gte=six_months_ago) \
            .values('customer') \
            .annotate(total_spent=models.Sum('total_amount')) \
            .order_by('-total_spent')[:5]
        return top_customers
    
