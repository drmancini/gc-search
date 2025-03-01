
from math import sin

"""
  Definition of UKIDSS Large Area Survey (LAS) coverage areas.
  - L1 SDSS coordinates -36.25 < eta < -16.25, -60 < lambda < +53.
  - L2a, L2b
  - L3 includes SDSS Stripe 82 (-50 < RA < 59, -1.25 < DEC < 1.25)
  - L4 encloses the Herschel-ATLAS northern field. This is a rectangular block measuring 15 degrees by 10 degrees centred on RA=199.5, Dec=29 and rotated by 8 degrees clockwise.

  Sources:
  - http://www.ukidss.org/surveys/surveys.html
  - https://classic.sdss.org/legacy/stripe82.php
  - https://www.h-atlas.org/survey/fields
  - https://www.sdss4.org/dr17/algorithms/surveycoords/
  """

l4_ra_offset = 7.5 * sin(8)
l4_dec_offset = 5 * sin(8)

LAS_COVERAGE = [
  {
    "name": "L1", # final
    "ra_from": 125,
    "ra_to": 238,
    "dec_from": -2,
    "dec_to": 15
  },
  {
    "name": "L2a",
    "ra_from": 114,
    "ra_to": 128,
    "dec_from": 18,
    "dec_to": 30
  },
  {
    "name": "L2b",
    "ra_from": 240,
    "ra_to": 250,
    "dec_from": 22,
    "dec_to": 32
  },
  {
    "name": "L3", # final
    "ra_from": -50,
    "ra_to": 60,
    "dec_from": -1.25,
    "dec_to": 1.25
  },
  {
    "name": "L4", # final
    "ra_from": 192 - l4_ra_offset,
    "ra_to": 207 + l4_ra_offset,
    "dec_from": 24 - l4_dec_offset,
    "dec_to": 29 + l4_dec_offset
  },
]

