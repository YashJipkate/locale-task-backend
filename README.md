# Backend Task for Locale

## Instructions to setup local environment

- Make sure PostgreSQL is installed. Find details [here](https://www.postgresql.org/download/).
- Make sure Python 3.8.5 and Pipenv installed.
- From the root of this folder, run `pipenv shell` to activate the virtual environment.
- Install the requirements by `pipenv install`
- Create a PostgreSQL table and fill in the credentials in `locale_backend/settings.py` in the `DATABASES` key.
- Run `python manage.py runserver` to fire up the local server.

## Testing the API

- Start the local server.
- Send a POST request to `http://127.0.0.1:8000/core/create_booking/` with the appropriate fields mentioned in the `models.py`.

### An example request

```
{
    "booking_id": "efsfczvdvs",
    "user_id": "fsrgsdf",
    "vehicle_model_id": "werwef",
    "package_id": 1,
    "travel_type_id": 2,
    "from_area_id": "kdfvkjsdv",
    "to_area_id": "fsfjnksjdf",
    "from_city_id": "aasbcjacshbd",
    "to_city_id": "sefsjebjefb",
    "from_date": "jewfbkjwbf",
    "to_date": "jsafkjaf",
    "online_booking": true,
    "mobile_site_booking": true,
    "booking_created": "sdvhbvjh",
    "from_lat": 32.342,
    "from_long": 45.232,
    "to_lat": 324.231,
    "to_long": 34.1234,
    "car_cancellation": 1
}
```

## Technology Stack
- Django
- Django Rest Framework
- PostgreSQL
