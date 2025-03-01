from config.constants import LAS_COVERAGE

def test_ukidss_footprint(ra, dec):
  for area in LAS_COVERAGE:
    if area['ra_from'] <= ra <= area['ra_to'] and area['dec_from'] <= dec <= area['dec_to']:
      return True
  return False