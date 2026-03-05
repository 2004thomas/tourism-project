from django.contrib import admin
from .models import Photo, Review, Place

# Register your models here.
admin.site.register(Place)
admin.site.register(Photo)
admin.site.register(Review)

# @admin.register(Place)
# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ('name','category')


# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('user', 'place', 'status', 'created_at')
#     list_filter = ('status',)
#     search_fields = ('user__username', 'place__name')