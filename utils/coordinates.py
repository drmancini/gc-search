from astropy.coordinates import SkyCoord
import astropy.units as u
from config.constants import LAS_COVERAGE

def test_ukidss_footprint(ra, dec):
  for area in LAS_COVERAGE:
    if area['ra_from'] <= ra <= area['ra_to'] and area['dec_from'] <= dec <= area['dec_to']:
      return True, area['name']
  return False, None

def coordinate_str2deg(ra_str, dec_str):
  coord = SkyCoord(ra=ra_str, dec=dec_str, unit=(u.hourangle, u.deg))
  return coord.ra.deg, coord.dec.deg