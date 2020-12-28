from django.db import models

# Create your models here.

class Booking(models.Model):
    PACKAGE_TYPES = [
        (1, '4hrs & 40kms'),
        (2, '8hrs & 80kms'),
        (3, '6hrs & 60kms'),
        (4, '10hrs & 100kms'),
        (5, '5hrs & 50kms'),
        (6, '3hrs & 30kms'),
        (7, '12hrs & 120kms'),
    ]
    TRAVEL_TYPES = [
        (1, 'long distance'),
        (2, 'point to point'),
        (3, 'hourly rental'),
    ]
    booking_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    vehicle_model_id = models.CharField(max_length=100)
    package_id = models.IntegerField(choices=PACKAGE_TYPES, default=1)
    travel_type_id = models.IntegerField(choices=TRAVEL_TYPES, default=1)
    from_area_id = models.CharField(max_length=100, blank=True)
    to_area_id = models.CharField(max_length=100, blank=True)
    from_city_id = models.CharField(max_length=100)
    to_city_id = models.CharField(max_length=100, blank=True)
    from_date = models.CharField(max_length=100)
    to_date = models.CharField(max_length=100)
    online_booking = models.BooleanField(default=True)
    mobile_site_booking = models.BooleanField(default=False)
    booking_created = models.CharField(max_length=100)
    from_lat = models.FloatField()
    from_long = models.FloatField()
    to_lat = models.FloatField()
    to_long = models.FloatField()
    car_cancellation = models.IntegerField(choices=[(1, '1'), (0, '0')], default=0)
