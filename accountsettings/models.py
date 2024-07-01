from django.db import models
from django.conf import settings

class SavedAddress(models.Model):
    COUNTRIES = [
        ('Afghanistan', 'Afghanistan'),
        ('ÅlandIslands', 'ÅlandIslands'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('AmericanSamoa', 'AmericanSamoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antarctica', 'Antarctica'),
        ('AntiguaandBarbuda', 'AntiguaandBarbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Aruba', 'Aruba'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('BosniaandHerzegovina', 'BosniaandHerzegovina'),
        ('Botswana', 'Botswana'),
        ('BouvetIsland', 'BouvetIsland'),
        ('Brazil', 'Brazil'),
        ('BritishIndianOceanTerritory', 'BritishIndianOceanTerritory'),
        ('BruneiDarussalam', 'BruneiDarussalam'),
        ('Bulgaria', 'Bulgaria'),
        ('BurkinaFaso', 'BurkinaFaso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('CapeVerde', 'CapeVerde'),
        ('CaymanIslands', 'CaymanIslands'),
        ('CentralAfricanRepublic', 'CentralAfricanRepublic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('ChristmasIsland', 'ChristmasIsland'),
        ('Cocos(Keeling)Islands', 'Cocos(Keeling)Islands'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Congo,TheDemocraticRepublicofThe', 'Congo,TheDemocraticRepublicofThe'),
        ('CookIslands', 'CookIslands'),
        ('CostaRica', 'CostaRica'),
        ("CoteD'ivoire", "CoteD'ivoire"),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('CzechRepublic', 'CzechRepublic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('DominicanRepublic', 'DominicanRepublic'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('ElSalvador', 'ElSalvador'),
        ('EquatorialGuinea', 'EquatorialGuinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('FalklandIslands(Malvinas)', 'FalklandIslands(Malvinas)'),
        ('FaroeIslands', 'FaroeIslands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('FrenchGuiana', 'FrenchGuiana'),
        ('FrenchPolynesia', 'FrenchPolynesia'),
        ('FrenchSouthernTerritories', 'FrenchSouthernTerritories'),
        ('Gabon', 'Gabon'),
        ('Gambia', 'Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Greenland', 'Greenland'),
        ('Grenada', 'Grenada'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Guam', 'Guam'),
        ('Guatemala', 'Guatemala'),
        ('Guernsey', 'Guernsey'),
        ('Guinea', 'Guinea'),
        ('Guinea-bissau', 'Guinea-bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('HeardIslandandMcdonaldIslands', 'HeardIslandandMcdonaldIslands'),
        ('HolySee(VaticanCityState)', 'HolySee(VaticanCityState)'),
        ('Honduras', 'Honduras'),
        ('HongKong', 'HongKong'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran,IslamicRepublicof', 'Iran,IslamicRepublicof'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('IsleofMan', 'IsleofMan'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jersey', 'Jersey'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ("Korea,DemocraticPeople'sRepublicof", "Korea,DemocraticPeople'sRepublicof"),
        ('Korea,Republicof', 'Korea,Republicof'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ("LaoPeople'sDemocraticRepublic", "LaoPeople'sDemocraticRepublic"),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('LibyanArabJamahiriya', 'LibyanArabJamahiriya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macao', 'Macao'),
        ('Macedonia,TheFormerYugoslavRepublicof', 'Macedonia,TheFormerYugoslavRepublicof'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('MarshallIslands', 'MarshallIslands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia,FederatedStatesof', 'Micronesia,FederatedStatesof'),
        ('Moldova,Republicof', 'Moldova,Republicof'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('NetherlandsAntilles', 'NetherlandsAntilles'),
        ('NewCaledonia', 'NewCaledonia'),
        ('NewZealand', 'NewZealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('NorfolkIsland', 'NorfolkIsland'),
        ('NorthernMarianaIslands', 'NorthernMarianaIslands'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('PalestinianTerritory,Occupied', 'PalestinianTerritory,Occupied'),
        ('Panama', 'Panama'),
        ('PapuaNewGuinea', 'PapuaNewGuinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Pitcairn', 'Pitcairn'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('PuertoRico', 'PuertoRico'),
        ('Qatar', 'Qatar'),
        ('Reunion', 'Reunion'),
        ('Romania', 'Romania'),
        ('RussianFederation', 'RussianFederation'),
        ('Rwanda', 'Rwanda'),
        ('SaintHelena', 'SaintHelena'),
        ('SaintKittsandNevis', 'SaintKittsandNevis'),
        ('SaintLucia', 'SaintLucia'),
        ('SaintPierreandMiquelon', 'SaintPierreandMiquelon'),
        ('SaintVincentandTheGrenadines', 'SaintVincentandTheGrenadines'),
        ('Samoa', 'Samoa'),
        ('SanMarino', 'SanMarino'),
        ('SaoTomeandPrincipe', 'SaoTomeandPrincipe'),
        ('SaudiArabia', 'SaudiArabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('SierraLeone', 'SierraLeone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('SolomonIslands', 'SolomonIslands'),
        ('Somalia', 'Somalia'),
        ('SouthAfrica', 'SouthAfrica'),
        ('SouthGeorgiaandTheSouthSandwichIslands', 'SouthGeorgiaandTheSouthSandwichIslands'),
        ('Spain', 'Spain'),
        ('SriLanka', 'SriLanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('SvalbardandJanMayen', 'SvalbardandJanMayen'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('SyrianArabRepublic', 'SyrianArabRepublic'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania,UnitedRepublicof', 'Tanzania,UnitedRepublicof'),
        ('Thailand', 'Thailand'),
        ('Timor-leste', 'Timor-leste'),
        ('Togo', 'Togo'),
        ('Tokelau', 'Tokelau'),
        ('Tonga', 'Tonga'),
        ('TrinidadandTobago', 'TrinidadandTobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('TurksandCaicosIslands', 'TurksandCaicosIslands'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('UnitedArabEmirates', 'UnitedArabEmirates'),
        ('UnitedKingdom', 'UnitedKingdom'),
        ('UnitedStates', 'UnitedStates'),
        ('UnitedStatesMinorOutlyingIslands', 'UnitedStatesMinorOutlyingIslands'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('VietNam', 'VietNam'),
        ('VirginIslands,British', 'VirginIslands,British'),
        ('VirginIslands,U.S.', 'VirginIslands,U.S.'),
        ('WallisandFutuna', 'WallisandFutuna'),
        ('WesternSahara', 'WesternSahara'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe')
    ]
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100,choices=COUNTRIES)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    
class SavedPayment(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    cardnumber = models.CharField(max_length=100)
    cardname = models.CharField(max_length=100)
    cardexp = models.CharField(max_length=100)
    cardcvv = models.CharField(max_length=100)
    paypalemail = models.CharField(max_length=100)
    type = models.IntegerField(default=0)

