from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from users.models import Customers

TABLE_NUMBERS = (
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
)

class Reservations(models.Model):
    now = timezone.now()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    email = models.CharField(default="")
    booking_id = models.AutoField(primary_key=True)
    table_number = models.CharField(
        max_length=20,
        choices=TABLE_NUMBERS,
        )
    date = models.DateField(max_length=20)
    start_time = models.TimeField(default=now.hour)
    end_time = models.TimeField(default=now.hour)
    active_booking = models.BooleanField(default=True)

    def __str__(self):
        return f"Reservation #{self.booking_id} - Email {self.user.email} Table No {self.table_number} - Date {self.date} - From {self.start_time} - Till {self.end_time} - Active? {self.active_booking}"