from django.contrib import admin
from .models import Property, PropertyImage, Bid, Testimonial, TeamMember

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'bedrooms', 'owner')
    search_fields = ('title', 'location')
    list_filter = ('location', 'bedrooms')

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image', 'description')
    search_fields = ('description',)
    list_filter = ('property',)

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('property', 'amount', 'bidder')
    search_fields = ('property__title', 'bidder__username')
    list_filter = ('property',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('property', 'user', 'rating')
    search_fields = ('property__title', 'user__username')
    list_filter = ('rating',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'contact_details')
    search_fields = ('name', 'role')
    list_filter = ('role',)
