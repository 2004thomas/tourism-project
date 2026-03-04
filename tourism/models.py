from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



#Create your models here


# def validate_review_length(value):
#     word_count = len(value.split())
#     if word_count < 100 or word_count > 150:
#         raise ValidationError("Review must be between 100 and 150 words.")

# def validate_image_size(image):
#     if image.size > 2 * 1024 * 1024:
#         raise ValidationError("Image must be under 2MB.")


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
    about=models.TextField(blank=True)
    highlights=models.TextField(blank=True)
    essential_info=models.TextField(blank=True)
    how_to_reach=models.TextField(blank=True)
    nearby_facilities=models.TextField(blank=True)
    booking_link=models.URLField(blank=True,null=True)
    latitude=models.FloatField(blank=True,null=True)
    longitude=models.FloatField(blank=True,null=True)
    # description = models.TextField()
    # main_image = models.ImageField(upload_to='places/')
    def __str__(self):
        return self.name

    # def __str__(self):
    #     place_name = self.place.name if self.place else "No Place"
    #     return f"{self.user.username} - {place_name}"


def validate_review_length(value):
    word_count = len(value.split())
    if word_count > 150:
        raise ValidationError("Review must be less than 150 words.")

def validate_image_size(image):
    if image.size > 2 * 1024 * 1024:
        raise ValidationError("Image must be under 2MB.")


class Review(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place
    ,on_delete=models.CASCADE)
    content = models.TextField(validators=[validate_review_length])
    image = models.ImageField(
        upload_to='reviews/',
        null=True,
        blank=True,
        validators=[validate_image_size]
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"

@property
def badge_color(self):
    colors={
        'nature':'success',
        'heritage':'warning',
        'pilgrimage':'danger',
        'hidden':'secondary'
    }