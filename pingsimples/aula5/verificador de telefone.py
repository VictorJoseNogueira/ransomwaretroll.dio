import phonenumbers
from phonenumbers import geocoder
fone = input('Digite o numero no formato: +551140028922(apenas os numeros): ')

phone_number = phonenumbers.parse(fone)
print(geocoder.description_for_number(phone_number, 'pt'))
