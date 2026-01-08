from django.db import models


# Create your models here.
class Property(models.Model):
    SALE_CHOICES = (
        ('For Sale', 'For Sale'),
        ('For Rent', 'For Rent'),
    )

    PARKING_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    HOME_CHOICES = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Studio', 'Studio'),
    )

    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)  # Zipcode is better as 20 chars, not 100
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for prices
    description = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default value added
  # Same as above
    parking = models.CharField(max_length=10, choices=PARKING_CHOICES)  # Limit length to 10 (enough for choices)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sale_type = models.CharField(max_length=20, choices=SALE_CHOICES)  # Limit length to 20 (enough for choices)
    home_type = models.CharField(max_length=20, choices=HOME_CHOICES)  # Same as above
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
