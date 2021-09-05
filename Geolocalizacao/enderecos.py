from pygeocoder import Geocoder
# pegar variaveis de ambiente
from decouple import config

endereco =  'Avenida Paulista, 100, São Paulo'

endereco_completo = Geocoder(config('GEOCODE_KEY')).geocode(endereco)
print(endereco_completo)

estado = Geocoder(config('GEOCODE_KEY')).geocode(endereco).state
print(estado)

cep = Geocoder(config('GEOCODE_KEY')).geocode(endereco).postal_code
print(cep)

pais = Geocoder(config('GEOCODE_KEY')).geocode(endereco).country
print(pais)

latitude_longitude = Geocoder(config('GEOCODE_KEY')).geocode(endereco).coordinates
print(latitude_longitude)

print('\n Utilizando reverse_geocode\n')
latitude=-23.570807
longitude=-46.6444668
geocode_reverse=Geocoder(config('GEOCODE_KEY')).reverse_geocode(latitude, longitude)
print(geocode_reverse)
