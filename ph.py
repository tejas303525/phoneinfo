import phonenumbers
from phonenumbers import carrier,timezone,geocoder



mob=input("Enter the number with coountry code:")
mob=phonenumbers.parse(mob)

print("Validity-->",phonenumbers.is_valid_number(mob))
print("Name of the carrier-->",carrier.name_for_valid_number(mob,"en"))
print("Timezone of the number-->",timezone.time_zones_for_number(mob))
print("Country name-->",geocoder.country_name_for_number(mob,"en"))
print("Region information-->",geocoder.description_for_number(mob,"en"))
