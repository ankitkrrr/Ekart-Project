from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar','Bihar'),
    ('chandigarh', 'chandigarh'),
    ('chhattisgarh','chhatisgarh'),
    ('Dadra & Nagar Hawali', 'Dadra & Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('jammu & Kashmir', 'jammu & kashmir'),
    ('jharkhand','jharkand'),
    ('karnataka','karnataka'),
    ('kerala','kerala'),
    ('west Bengal','west Bengal'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    
    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
) 

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    Product_image = models.ImageField(upload_to='producting')
    
    def __str__(self):
        return str(self.id)
    
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
        

STATE_CHOICES = (
    ('Acceptecd', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50,choices=STATE_CHOICES , default='pending') 


 