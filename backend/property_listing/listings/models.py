from django.contrib.auth.models import User
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.FloatField()
    bedrooms = models.IntegerField()
    owner = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.property.title} - {self.id}'
        
class Bid(models.Model):
    amount = models.FloatField()
    bidder = models.ForeignKey(User, related_name='bids', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='bids', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bidder.username} - {self.amount}"

class Testimonial(models.Model):
    property = models.ForeignKey(Property, related_name='testimonials', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='testimonials', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.rating}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=150)

    def __str__(self):
        return self.name
