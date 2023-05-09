from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Vyrobce(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name='Název výrobce', help_text='Zadejte název výrobce aut')
    datum = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False,verbose_name='Datum založení', help_text='Zadejte datum založení firmy')
    zeme = models.CharField(max_length=100, null=False, verbose_name='Země původu', help_text='Zadejte zemi, ze které firma pochází')

    class Meta:
        verbose_name = 'Výrobce'
        verbose_name_plural = 'Výrobci'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev

class Auto(models.Model):
    MODELY_AUT = [
        ("sedan", "Sedan"),
        ("suv", "SUV"),
        ("off road", "Off road"),
        ("kupé", "Kupé"),
        ("kabriolet", "Kabriolet"),
        ("dodávka", "Dodávka")
    ]
    PALIVA = [
        ("benzín", "Benzín"),
        ("nafta", "Nafta"),
        ("elektro", "Elektro"),
        ("hybrid", "Hybrid")
    ]

    nazev = models.CharField(max_length=50, null=False, blank=False,verbose_name='Název auta', help_text='Zadejte název auta')
    model_auta = models.CharField(max_length= 100, verbose_name='Model auta', help_text='Vyberte model auta', default='Sedan', choices=MODELY_AUT)
    cena = models.PositiveIntegerField(null=False, blank=False,verbose_name='Cena auta', help_text='Zadejte cenu auta')
    rok_vyroby = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Rok výroby', help_text='Zadejte rok výroby auta')
    palivo = models.CharField(max_length=100, verbose_name='Palivo', help_text='Vyberte co používá auto za pohonou hmotu', choices=PALIVA)
    znacka = models.ForeignKey('Vyrobce', on_delete=models.CASCADE, verbose_name='Značka', help_text='Vyberte značku auta', default=0)
    autobazar = models.ManyToManyField('Autobazar', verbose_name='Autobazar', help_text='Vyberte autobazar, ve kterém se auto nachází')

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Auta'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev
    
class Autobazar(models.Model):
    nazev = models.CharField(max_length=100, null=False, blank=False, verbose_name='Název autobazaru', help_text='Zadejte název autobazaru')
    obec = models.CharField(max_length=100, null=False, blank=False, verbose_name='Obec', help_text='Zadejte obec, ve které se autobazar nachází')
    ulice = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ulice', help_text='Zadejte ulici, ve které se autobazar nachází')
    psc = models.PositiveIntegerField(null=False, blank=False, verbose_name='PSČ', help_text='Zadejte PSČ')
    
    class Meta:
        verbose_name = 'Autobazar'
        verbose_name_plural = 'Autobazary'
        ordering = ['nazev']

    def __str__(self):
        return self.nazev
    
class Zamestnanec(models.Model):
    jmeno = models.CharField(max_length=50, null=False, blank=False, verbose_name='Jméno zaměstnance', help_text='Zadejte jméno zaměstnance')
    prijmeni = models.CharField(max_length=50, null=False, blank=False, verbose_name='Příjmení zaměstnance', help_text='Zadejte příjmení zaměstnance')
    obec = models.CharField(max_length=100, null=False, blank=False, verbose_name='Obec', help_text='Zadejte obec, ve které zaměstnanec bydlí')
    ulice = models.CharField(max_length=50, null=True, verbose_name='Ulice', help_text='Zadejte ulici, ve které zaměstnanec bydlí')
    cislo_popisne = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Číslo popisné', help_text='Zadejte číslo popisné')
    psc = models.PositiveIntegerField(null=False, blank=False, verbose_name='PSČ', help_text='Zadejte PSČ')
    telefon = models.CharField(max_length=20, verbose_name='Telefon', help_text='Zadejte telefonní číslo zaměstnance (včetně předvolby)',
                               validators=[RegexValidator(regex='^(\\+420)? ?[1-9][0-9]{2}( ?[0-9]{3}){2}$',message='Zadejte prosím platné telefonní číslo.')])
    fotka = models.ImageField(upload_to='zamestnanci', null=True, blank=True, verbose_name='Fotka zaměstnance', help_text='Nahrejte fotku zaměstnance')
    autobazar = models.ForeignKey('Autobazar', on_delete=models.CASCADE, verbose_name='Autobazar', help_text='Vyberte autobazar, ve kterém zaměstnanec pracuje', default=0)
    
    class Meta:
        verbose_name = 'Zaměstnanec'
        verbose_name_plural = 'Zaměstnanci'
        ordering = ['prijmeni', 'jmeno']

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'