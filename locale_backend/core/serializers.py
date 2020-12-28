from rest_framework import serializers

from locale_backend.core.models import *

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'booking_id', 'user_id', 'vehicle_model_id', 'package_id', 'travel_type_id', 'from_area_id',
            'to_area_id', 'from_city_id', 'to_city_id', 'from_date', 'to_date', 'online_booking',
            'mobile_site_booking', 'booking_created', 'from_lat', 'from_long', 'to_lat', 'to_long',
            'car_cancellation']

    def validate(self, data):
        travel_type_id = data['travel_type_id']
        from_area_id = data.get('from_area_id')
        to_area_id = data.get('to_area_id')
        if travel_type_id != 2:
            if from_area_id != None:
                raise serializers.ValidationError('`from_area_id` is applicable only for point-to-point travel')
            if to_area_id != None:
                raise serializers.ValidationError('`to_area_id` is applicable only for point-to-point travel')
        return data