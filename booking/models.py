from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

NUMBER_OF_SEATS = [
    ('2', '2'),
    ('4', '4'),
    ('6', '6'),
    ('8', '8')
]

ROOM_NAME = [
    ('Main Bar', 'Main Bar'),
    ('Dining Room', 'Dining Room'),
    ('Sports Room', 'Sports Room')
]

TABLE_NUMBERS = [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
    ('45', '45'),
    ('46', '46'),
    ('47', '47'),
    ('48', '48'),
    ('49', '49'),
    ('50', '50'),
    ('51', '51'),
    ('52', '52'),
    ('53', '53'),
    ('54', '54'),
    ('55', '55'),
    ('56', '56'),
    ('57', '57'),
    ('58', '58'),
    ('59', '59'),
    ('60', '60'),
    ('61', '61')
]

class Calender(models.Model):
    choose_date = models.DateField()

class Tables(models.Model):
    table_number = models.IntegerField(primary_key=True)
    no_of_seats = models.IntegerField(choices=NUMBER_OF_SEATS)
    room_type = models.CharField(max_length=12, choices=ROOM_NAME)
    available = models.BooleanField()


class Reservations(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    date_and_time = models.DateTimeField()
    booking_length = models.DurationField()
    table_number = models.IntegerField(choices=TABLE_NUMBERS)
