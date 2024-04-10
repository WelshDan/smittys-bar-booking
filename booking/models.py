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
    email = models.EmailField(Customers, default="", null=False, blank=False)
    booking_id = models.IntegerField(
        primary_key=True,
        auto_created = True,
        serialize=False,
        )
    table_number = models.CharField(
        max_length=20,
        choices=TABLE_NUMBERS,
        null=False,
        blank=False
        )
    date = models.DateField(max_length=20, null=False, blank=False)
    start_time = models.TimeField(default=now.hour, null=False, blank=False)
    end_time = models.TimeField(default=now.hour, null=False, blank=False)
    active_booking = models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation #{self.booking_id} - {self.user.username}"