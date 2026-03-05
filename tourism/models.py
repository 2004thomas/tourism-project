from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Place(models.Model):

    CATEGORY_CHOICES=[
        ('nature','Nature'),
        ('pilgrimage','Pilgrimage'),
        ('heritage','Heritage'),
        ('hidden','Hidden')
    ]

    name = models.CharField(max_length=200,unique=True)
    hero_image=models.URLField(blank=True)
    tagline=models.CharField(max_length=300,blank=True)
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,null=True,blank=True)
    about=models.TextField(blank=True,null=True)
    highlights=models.TextField(blank=True,null=True)
    essential_info=models.TextField(blank=True,null=True)
    trekking_info=models.TextField(blank=True,null=True)
    safety_tips=models.TextField(blank=True,null=True)
    entry_booking=models.TextField(blank=True,null=True)
    how_to_reach=models.TextField(blank=True,null=True)
    nearby_facilities=models.TextField(blank=True,null=True)
    booking_link=models.URLField(blank=True,null=True)
    latitude=models.FloatField(blank=True,null=True)
    longitude=models.FloatField(blank=True,null=True)
    def __str__(self):
        return self.name
def validate_review_length(value):
    word_count = len(value.split())
    if word_count > 150:
        raise ValidationError("Review must be less than 150 words.")

def validate_image_size(image):
    if image.size > 2 * 1024 * 1024:
        raise ValidationError("Image must be under 2MB.")

class Photo(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='place_photos/')
    approved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.place.name} photo"

class Review(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.place.name} review"

@property
def badge_color(self):
    colors={
        'nature':'success',
        'heritage':'warning',
        'pilgrimage':'danger',
        'hidden':'secondary'
    }