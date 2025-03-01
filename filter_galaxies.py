"""
Scans the Updated nearby galaxy catalog by Karachentsev et al. (2013) for galaxies within UKIDSS LAS coverage areas.
"""

from astropy.coordinates import SkyCoord
import astropy.units as u
from astroquery.vizier import Vizier
Vizier.ROW_LIMIT = -1

from config.constants import LAS_COVERAGE
import json

output_file = '../data/raw/galaxies.json'

distance_from = 1.5 # Mpc
distance_to = 15 # Mpc
diameter_from = 5 # kpc

# Query Vizier for data
galaxy_catalogs = Vizier.get_catalogs('J/AJ/145/101')
gc_galaxies = Vizier.get_catalogs('J/ApJ/772/82')
# legus_galaxies = Vizier.get_catalogs('J/ApJS/235/23/table4')

galaxy_data = galaxy_catalogs[0].to_pandas().to_dict(orient='records')
# legus_data = legus_galaxies[0].to_pandas().to_dict(orient='records')

print(f"Found {len(galaxy_data)} galaxies in catalog")

# Convert RA and DEC from string to degrees
for entry in galaxy_data:
  ra_str = entry['RAJ2000']
  dec_str = entry['DEJ2000']
  coord = SkyCoord(ra=ra_str, dec=dec_str, unit=(u.hourangle, u.deg))
  entry['RAJ2000'] = coord.ra.deg
  entry['DEJ2000'] = coord.dec.deg

# Flag the results to only include galaxies within the UKIDSS LAS coverage areas
data_in_survey = []
for entry in galaxy_data:
  for area in LAS_COVERAGE:
    if area['ra_from'] <= entry['RAJ2000'] <= area['ra_to'] and area['dec_from'] <= entry['DEJ2000'] <= area['dec_to']:
      entry['LAS_coverage'] = area['name']
      data_in_survey.append(entry)

print(f"... {len(data_in_survey)} galaxies fit inside UKIDSS LAS coverage areas")

# Filter the results to only include galaxies within the specified distance range
data_at_distance = []
for entry in data_in_survey:
  if distance_from <= entry['Dist'] <= distance_to:
    data_at_distance.append(entry)

print(f"... {len(data_at_distance)} galaxies fit inside distance range")

# Filter the results to only include galaxies with radius larger than the specified value
data_with_radius = []
for entry in data_at_distance:
  if entry['A26'] >= diameter_from:
      data_with_radius.append(entry)

print(f"... {len(data_with_radius)} galaxies have radius larger than {diameter_from} kpc")

# Filter the results to only include galaxies in the LEGUS catalog
# galaxies_in_legus = []
# for entry in data_with_radius:
#   for legus_entry in legus_data:
#     if entry['Name'] == legus_entry['Name'].replace(" ", ""):
#       galaxies_in_legus.append(entry)

# print(f"... {len(galaxies_in_legus)} galaxies are in LEGUS catalog")

# Write the data to a JSON file
with open(output_file, 'w') as f:
  # json.dump(galaxies_in_legus, f, indent=4)
  json.dump(data_with_radius, f, indent=4)

print(f"Data written to {output_file}")