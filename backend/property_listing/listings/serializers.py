from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Property, PropertyImage , Bid, Testimonial, TeamMember

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image', 'description']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'location', 'price', 'bedrooms', 'owner', 'images']

class BidSerializer(serializers.ModelSerializer):
    bidder = UserSerializer(read_only=True)
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Bid
        fields = ['id', 'amount', 'bidder', 'property']

class TestimonialSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Testimonial
        fields = ['id', 'rating', 'review', 'user', 'property']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'contact_details']
