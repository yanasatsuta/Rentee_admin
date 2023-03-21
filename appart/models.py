from django.db import models
from multiselectfield import MultiSelectField


class RentUser(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=150)
    last_name = models.CharField(verbose_name='Surname', max_length=150)
    username = models.CharField(verbose_name='Telegram Username', max_length=150, blank=True, null=True)
    tg_id = models.BigIntegerField(verbose_name='Telegram ID', null=False, unique=True)
    phone = models.CharField(verbose_name='Phone Number', max_length=15, null=True)
    register = models.DateTimeField(verbose_name='Date Registration', null=False)
    last_activity = models.DateTimeField(verbose_name='Last Activity', null=False)
    LANGUAGE = [
        ("EN", "English"),
        ("RU", "Русский"),
        ("IN", "Indonesian")
    ]
    default_lang = models.CharField(verbose_name='Default language', null=False, choices=LANGUAGE, max_length=2,
                                    default=None)
    subscribe = models.BooleanField(verbose_name='Activity subscribe', default=False)

    def __str__(self):
        return f'Telegram Username: {self.username}, Telegram ID: {self.tg_id}'


class Location(models.Model):
    name = models.CharField(verbose_name='Location Name', max_length=150)

    def __str__(self):
        return f'Location: {self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to=f'images/')

    def __str__(self):
        return f'Image ID: {self.id}'


class Apartment(models.Model):
    link = models.URLField(verbose_name='Link to original source')
    agent_name = models.CharField(verbose_name='Agent Name', max_length=150, blank=True, null=True)
    agent_whats_up = models.URLField(verbose_name='Agent Whats App', blank=True, null=True)
    APS_TYPE = [
        ('VI', 'Villa Entirely'),
        ('RO', 'Room in shared villa'),
        ('AP', 'Apartment'),
        ('GH', 'Guesthouse')
    ]
    aps_type = models.CharField(verbose_name='Apartment type', max_length=2, choices=APS_TYPE, null=False, default=None)
    location = models.ForeignKey(Location, verbose_name='Location', on_delete=models.CASCADE, null=False)
    bedroom = models.CharField(verbose_name='No. of bedrooms', max_length=5, null=False)
    AMENITIES = (('Kitchen', 'Kitchen'),
                 ('AC', 'AC'),
                 ('Private pool', 'Private pool'),
                 ('Shared pool', 'Shared pool'),
                 ('Wi-Fi', 'Wi-Fi'),
                 ('Shower', 'Shower'),
                 ('Bathtub', 'Bathtub'),
                 ('Cleaning service', 'Cleaning service'),
                 ('TV', 'TV'),
                 ('Parking area', 'Parking area'))
    amenities = MultiSelectField(verbose_name='Amenities', max_length=244, choices=AMENITIES, blank=True, null=True)
    images = models.ManyToManyField(Image, verbose_name='Images', blank=True)
    RENT_TERM = [('DAY', 'DAY'),
                 ('MONTH', 'MONTH'),
                 ('YEAR', 'YEAR')]
    rent_term = models.CharField(verbose_name='Rental term', max_length=5, choices=RENT_TERM, blank=True, null=True)
    price_rup = models.BigIntegerField(verbose_name='Price in Rupee', blank=True, null=True)
    price_usd = models.BigIntegerField(verbose_name='Price in USD', blank=True, null=True)
    description = models.CharField(verbose_name='Description', max_length=900, blank=True, null=True)

    def __str__(self):
        return f'Unique ID: {self.id}'


class Feedback(models.Model):
    type_a = models.CharField(verbose_name='Type of appeal', max_length=155, null=False)
    user = models.ForeignKey(RentUser, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Type {self.type_a}, Text: {self.text}'


class SaveAps(models.Model):
    user = models.ForeignKey(RentUser, verbose_name='User Name', on_delete=models.CASCADE)
    apart = models.ForeignKey(Apartment, verbose_name='Apartment ID', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'apart'),)

    def __str__(self):
        return f'User: {self.user}, Apartment: {self.apart}'
