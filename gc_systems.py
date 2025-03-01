"""
Scans the Catalog of globular cluster systems (Harris+, 2013) for galaxies with GCs within UKIDSS LAS coverage areas.
"""

from astropy.coordinates import SkyCoord
import astropy.units as u
from astroquery.vizier import Vizier
Vizier.ROW_LIMIT = -1

from utils.coordinates import test_ukidss_footprint
from config.constants import LAS_COVERAGE
import json

output_file = '../data/raw/gc_systems.json'

distance_from = 0 # Mpc
distance_to = 13 # Mpc
diameter_from = 0 # kpc
gc_count = 1

# Query Vizier for data
gc_galaxies = Vizier.get_catalogs('J/ApJ/772/82')

galaxy_data = gc_galaxies[0].to_pandas().to_dict(orient='records')

print(f"Found {len(galaxy_data)} galaxies in catalog")

# Flag the results to only include galaxies within the UKIDSS LAS coverage areas
data_in_survey = []
for entry in galaxy_data:
  ukidss_test = test_ukidss_footprint(entry['RAJ2000'], entry['DEJ2000'])
  if ukidss_test[0]:
    entry['UKIDSS_area'] = ukidss_test[1]
    data_in_survey.append(entry)

print(f"... {len(data_in_survey)} galaxies fit inside UKIDSS LAS coverage areas")

# Filter the results to only include galaxies within the specified distance range
data_at_distance = []
for entry in data_in_survey:
  if distance_from <= entry['Dist'] <= distance_to:
    data_at_distance.append(entry)

print(f"... {len(data_at_distance)} galaxies fit inside distance range")

# Filter the results to only include galaxies with large number of GCs
data_with_gc_count = []
for entry in data_at_distance:
  if entry['Ngc'] >= gc_count:
      data_with_gc_count.append(entry)

print(f"... {len(data_with_gc_count)} galaxies have at least {gc_count} GCs")

# Filter the results to only include galaxies with large number of GCs
data_with_radius = []
for entry in data_with_gc_count:
  if entry['Reff'] >= diameter_from:
      data_with_radius.append(entry)

print(f"... {len(data_with_radius)} galaxies have radius larger than {diameter_from} kpc")

# Write the data to a JSON file
with open(output_file, 'w') as f:
  json.dump(data_with_radius, f, indent=4)

print(f"Data written to {output_file}")

# NGC3384 - 
# NGC3384 - 
# NGC3384 - 
# NGC4517 - VI photometry of globular cluster systems (Goudfrooij+, 2003) https://arxiv.org/abs/astro-ph/0304195