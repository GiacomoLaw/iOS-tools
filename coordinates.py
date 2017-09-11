# get your coordinates

import location
address_dict = {'Street': 'Infinite Loop', 'City': 'Cupertino', 'Country': 'USA'}
results = location.geocode(address_dict)
print(results)