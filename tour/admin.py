
from django.contrib import admin

from tour.models import Booking, Category, Review, Tour

# Register your models here.

admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Booking)
