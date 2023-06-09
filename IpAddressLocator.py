import geocoder as geo

ip=geo.ip('me')
print(ip)
print(ip.city)