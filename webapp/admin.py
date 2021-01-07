from django.contrib import admin
from webapp.models import Theatre, Movie, Show, Booking, Seat, BookedSeat

# Register your models here.
admin.site.register(Theatre)
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Booking)
admin.site.register(Seat)
admin.site.register(BookedSeat)
