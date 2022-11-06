from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import CASCADE


# from django.db.models.functions import Cast

# Create your models here.

class Realtor(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    realtor_image = models.ImageField(help_text="Add realestate images", null=True, blank=True)
    bio = models.TextField(max_length=250, default="")
    TITLE = [
        ('Asystent/ka Biura', 'Asystent/ka Biura'),
        ('Młodszy Doradca ds. Nieruchomości', 'Młodszy Doradca ds. Nieruchomości'),
        ('Doradca ds. Nieruchomości', 'Doradca ds. Nieruchomości'),
        ('Starszy Doradca ds. Nieruchomości', 'Starszy Doradca ds. Nieruchomości'),
    ]
    title = models.CharField(max_length=35, choices=TITLE, null=True, blank=True,
                             help_text="What position in the company?")

    def __str__(self):
        if self.user is not None:
            return f'ID:{self.pk} | {self.user.first_name} {self.user.last_name}'
        return "brak użytkownika"

class RealestateType(models.Model):
    contact_data = models.TextField(max_length=100,
                                    help_text="Please leave Your Name and Phone Number, we will call you within 24h")
    REALESTATE_TYPE = [
        ('Apartament', 'Apartament'),
        ('Mieszkanie', 'Mieszkanie'),
        ('Dom', 'Dom'),
        ('Działka', 'Działka'),
        ('Lokale', 'Lokale'),
        ('Obiekty', 'Obiekty'),
        ('Inny', 'Inny'),
    ]
    name = models.CharField(max_length=12, choices=REALESTATE_TYPE, null=True, blank=True,
                            help_text="What type is the realestate?")
    CONDITION = [
        ('Zrobione Pod Klucz', 'Zrobione Pod Klucz'),
        ('Do remontu', 'Do remontu'),
        ('Do odświeżenia', 'Do odświeżenia'),
        ('Stan deweloperski', 'Stan deweloperski'),
        ('Działka budowlana', 'Działka budowlana'),
        ('Działka leśna', 'Działka leśna'),
        ('Działka rolna', 'Działka rolna'),
        ('Inny', 'Inny'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION, null=True, blank=True,
                                 help_text="What is the realestate "
                                           "condition?")

    def __str__(self):
        return f'{self.name} {self.condition}'


class Realestate(models.Model):
    date_addet = models.DateField(null=True, blank=True)
    date_when_aviable = models.TimeField(null=True, blank=True)
    realestate_image = models.ImageField(null=True, blank=True, help_text="Add realestate images")
    price = models.IntegerField(null=True, blank=True, help_text="What is the PRICE?")
    area = models.IntegerField(null=True, blank=True, help_text="Square meters?")
    location = models.CharField(max_length=100, null=True, blank=True, help_text="What is realestate address?")
    OWNERSHIP = [
        ('Brak', 'Brak'),
        ('Własność', 'Własność'),
        ('Spółdzielcze własnościowe prawo', 'Spółdzielcze własnościowe prawo'),
        ('Udział', 'Udział'),
        ('Spółdzielcze lokatorskie prawo', 'Spółdzielcze lokatorskie prawo'),
        ('Inne', 'Inne'),
    ]
    ownership = models.CharField(max_length=40, choices=OWNERSHIP, null=True, blank=True, help_text="What type of "
                                                                                                    "ownership law?")
    area_land = models.IntegerField(null=True, blank=True, help_text="What is the land area?")
    LAND_SHAPE = [
        ('Brak', 'Brak'),
        ('Nieregularny', 'Nieregularny'),
        ('Kwadrat', 'Kwadrat'),
        ('Prostokąt', 'Prostokąt'),
        ('Trapez', 'Trapez'),
        ('Trójkąt', 'Trójkąt'),
        ('Inne', 'Inne'),
    ]
    land_shape = models.CharField(max_length=13, choices=LAND_SHAPE, null=True, blank=True,
                                  help_text="What shape is the land?")
    DRIVE = [
        ('Brak', 'Brak'),
        ('Asfaltowy', 'Asfaltowy'),
        ('Utwardzany', 'Utwardzany'),
        ('Kostka brukowa', 'Kostka brukowa'),
        ('inny', 'inny'),
    ]
    drive = models.CharField(max_length=15, choices=DRIVE, null=True, blank=True, help_text="What type of drive?")
    rooms = models.IntegerField(null=True, blank=True, help_text="How many rooms?")
    floor = models.IntegerField(null=True, blank=True, help_text="What floor is it?")
    floors = models.IntegerField(null=True, blank=True, help_text="How many floors the building has?")
    MARKET = [
        ('Wtórny', 'Wtórny'),
        ('Pierwotny', 'Pierwotny'),
    ]
    market = models.CharField(max_length=10, choices=MARKET, null=True, blank=True, help_text="What type of market?")
    BUILDING_MATERIAL = [
        ('Brak', 'Brak'),
        ('Cegła', 'Cegła'),
        ('Pustak', 'Pustak'),
        ('Ytong', 'Ytong'),
        ('Beton', 'Beton'),
        ('Inny', 'Inny'),
    ]
    building_material = models.CharField(max_length=8, choices=BUILDING_MATERIAL, null=True, blank=True,
                                         help_text="What was used "
                                                   "to build?")
    ROOF = [
        ('Brak', 'Brak'),
        ('Płaski', 'Płaski'),
        ('Jednospadowy', 'Jednospadowy'),
        ('Dwuspadowy', 'Dwuspadowy'),
        ('Wielospadowy', 'Wielospadowy'),
        ('Inny', 'Inny'),
    ]
    roof = models.CharField(max_length=14, choices=ROOF, blank=True, null=True,  help_text="What type of roof?")
    ROOF_MATERIAL = [
        ('Brak', 'Brak'),
        ('Papa', 'Papa'),
        ('Dachówka', 'Dachówka'),
        ('Blacha', 'Blacha'),
        ('Inny', 'Inny'),
    ]
    roof_material = models.CharField(max_length=10, choices=ROOF_MATERIAL, blank=True, null=True,
                                     help_text="The roof is made of?")
    MEDIA = [
        ('1', 'TAK'),
        ('2', 'NIE'),
    ]
    media = models.CharField(max_length=5, choices=MEDIA, blank=True, null=True, help_text="Are media available?")

    def __str__(self):
        return f'{self.ownership} {self.land_shape}' \
               f' {self.drive} {self.market}' \
               f' {self.building_material} {self.roof}' \
               f' {self.roof_material} {self.media}'



class Contact(models.Model):
    contact_image = models.ImageField(null=True, blank=True, help_text="Add contact image/s")
    contact_shieeetnigga = models.TextField(max_length=255, default="")
