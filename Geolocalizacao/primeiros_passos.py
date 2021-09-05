from pygeocoder import Geocoder
# pegar variaveis de ambiente
from decouple import config

endereco = '1222, Lins de Vascocelos, São Paulo, SP'
print(Geocoder(config('GEOCODE_KEY')).geocode(endereco).coordinates)